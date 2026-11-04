# StartupExcuses source security review — 2026-11-04

Reviewed the user-provided `StartupExcuses-source-review.tar.gz` **without
executing its code**. Files: `app.py`, `requirements.txt`, `startup-excuses.conf`,
`templates/index.html`.

## What was found

- No live AWS access keys, GitHub tokens, private SSH keys, RDS passwords, or
  `.env` file were found in the supplied archive.
- `app.py` originally used a predictable literal password fallback (`password`).
  The GitHub-safe copy removes that fallback and requires `DB_PASSWORD`.
- Dynamic `CREATE DATABASE` SQL previously embedded a database identifier with
  an f-string. The GitHub-safe copy uses `psycopg2.sql.Identifier`.
- The redundant `dotenv` package dependency was removed; `python-dotenv`
  provides `import dotenv`.
- `.env.example` contains **only fabricated placeholders**.

## Outstanding security work

- Nginx listens on HTTP port 80; HTTPS and safe redirect need configuration.
- Public excuse submission and voting have no authentication/rate limiting.
- Voting changes state through a GET route and has no CSRF protection.
- Input length limits, error handling, and monitoring should be hardened.
- `requirements.txt` dependencies are not version-pinned and need review.
- `init_db()` runs only when app.py is started directly, not via Gunicorn.
- This is a source-only review, not a runtime vulnerability assessment.

## Scope

The reviewed copy is separate from the live AWS instance: publishing this copy
**does not apply these fixes** to the currently deployed application. Never
upload live `.env` values or private keys to GitHub. Keep the repository private
until all file history, images, and configuration have been reviewed.
