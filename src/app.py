
import os
from datetime import datetime, timezone

import boto3
import dotenv
import psycopg2
from flask import Flask, redirect, render_template, request, url_for
from psycopg2 import sql


dotenv.load_dotenv()

app = Flask(__name__)


# CloudWatch custom application metrics
cloudwatch = boto3.client(
    "cloudwatch",
    region_name="eu-west-3"
)


def send_custom_metric(metric_name, value, unit="Count"):
    try:
        cloudwatch.put_metric_data(
            Namespace="StartupExcuses/Application",
            MetricData=[
                {
                    "MetricName": metric_name,
                    "Value": value,
                    "Unit": unit,
                    "Timestamp": datetime.now(timezone.utc),
                }
            ],
        )
    except Exception:
        app.logger.exception(
            "Unable to publish CloudWatch metric: %s",
            metric_name,
        )


# Database connection
def get_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        database=os.getenv("DB_NAME", "startup_excuses"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.environ["DB_PASSWORD"],
        port=os.getenv("DB_PORT", "5432"),
    )


def init_db():
    try:
        print("Checking/creating database...")

        # First, connect to default postgres database to create our database
        default_conn = psycopg2.connect(
            host=os.getenv("DB_HOST", "localhost"),
            database="postgres",  # Connect to default database
            user=os.getenv("DB_USER", "postgres"),
            password=os.environ["DB_PASSWORD"],
            port=os.getenv("DB_PORT", "5432"),
        )
        default_conn.autocommit = True

        with default_conn.cursor() as cur:
            # Check if our database exists
            cur.execute(
                "SELECT 1 FROM pg_database WHERE datname = %s",
                [os.getenv("DB_NAME", "startup_excuses")],
            )
            exists = cur.fetchone()

            if not exists:
                cur.execute(
                    sql.SQL("CREATE DATABASE {}").format(
                        sql.Identifier(os.getenv("DB_NAME", "startup_excuses"))
                    )
                )
                print(f"Database {os.getenv('DB_NAME', 'startup_excuses')} created")

        default_conn.close()

        # Now connect to our application database and create tables
        print("Initializing tables...")
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS excuses (
                        id SERIAL PRIMARY KEY,
                        excuse TEXT NOT NULL,
                        votes INTEGER DEFAULT 0,
                        submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """
                )
                print("Database initialized")
    except Exception as e:
        print(f"Error initializing database: {e}")
        raise e


@app.route("/")
def home():
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, excuse, votes FROM excuses ORDER BY votes DESC LIMIT 10"
            )
            top_excuses = cur.fetchall()

    send_custom_metric("PageViews", 1)
    return render_template("index.html", excuses=top_excuses)


@app.route("/submit", methods=["POST"])
def submit_excuse():
    excuse = request.form["excuse"]

    if excuse.strip():
        with get_db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO excuses (excuse) VALUES (%s)",
                    (excuse,)
                )

        send_custom_metric("ExcuseSubmissions", 1)

    return redirect(url_for("home"))



@app.route("/vote/<int:excuse_id>")
def vote(excuse_id):
    with get_db() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "UPDATE excuses SET votes = votes + 1 WHERE id = %s", (excuse_id,)
            )
    return redirect(url_for("home"))


@app.route("/health")
def health():
    return {"status": "healthy", "app": "StartupExcuses"}, 200


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
