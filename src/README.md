# StartupExcuses application source

This directory contains the **reviewed source copy** for the AWS lab, not a
live deployment. The deployed EC2 server is unchanged.

## Runtime

- Python / Flask; PostgreSQL (psycopg2); environment variables loaded via
  python-dotenv for local development.
- `DB_PASSWORD` is **required**. Keep it in EC2 service environment / secured
  secret handling, never in Git or an uploaded screenshot.
- Use `.env.example` as a field reference; it contains placeholders only.
- `python app.py` starts Flask's development server, **not a production server**.
- Nginx configuration in `startup-excuses.conf` listens on HTTP port 80,
  as demonstrated in the lab; a public production deployment needs HTTPS.
- For production, start the Flask application via a WSGI server (as in the lab,
  using Gunicorn); ensure database schema is initialized separately because
  `init_db()` is invoked only in the `__main__` code path.

## Security notes

This teaching demo has no user authentication, CSRF protection, rate limits, or
abuse prevention. Its vote endpoint changes state via GET, which should be
changed to an authenticated/CSRF-protected POST endpoint before production use.
Input length limits and comprehensive monitoring should also be added.
Database access requires appropriate least-privilege PostgreSQL credentials.

The source archive was reviewed for accidental secrets, not penetration tested.
