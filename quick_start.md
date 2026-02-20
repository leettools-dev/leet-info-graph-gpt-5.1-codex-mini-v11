# Quick Start

## Environment Variables
- `GOOGLE_CLIENT_ID` & `GOOGLE_CLIENT_SECRET` — credentials for Google OAuth (create in Google Cloud Console).
- `BACKEND_PORT` — port for the FastAPI backend (default: `8000`).
- `FRONTEND_PORT` — port for the frontend dev server (default: `3000`).
- `OPENAI_API_KEY` — (optional) API key for downstream AI services.

Store sensitive values in `.env` (ignored by git). Example `.env` entries:

```
GOOGLE_CLIENT_ID=AIza...
GOOGLE_CLIENT_SECRET=secret
BACKEND_PORT=8000
FRONTEND_PORT=3000
OPENAI_API_KEY=sk-...
```

## Local Setup
1. Backend
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r backend/requirements.txt
   ```
2. Frontend
   ```bash
   cd frontend
   npm install
   ```

## Starting Services
`./start.sh` handles clean startup:
- Stops prior backend/frontend processes using `pids/*.pid` files.
- Launches backend via `uvicorn backend.app.main:app --host 0.0.0.0 --port $BACKEND_PORT`.
- Launches frontend via `npm --prefix frontend run dev -- --host 0.0.0.0 --port $FRONTEND_PORT`.
- Logs go to `logs/backend.log` and `logs/frontend.log`.
- PID files go to `pids/backend.pid` and `pids/frontend.pid`.
- At the end it prints the URLs you can visit:
  - Backend: `http://localhost:${BACKEND_PORT}`
  - Frontend: `http://localhost:${FRONTEND_PORT}`

## Stopping Services
`./stop.sh` reads each PID file from `pids/` and gracefully stops the process, cleaning up log/pid entries.

## Docker
1. Build and run all services:
   ```bash
   docker compose up --build
   ```
2. Visit `http://localhost:3000` for the frontend and `http://localhost:8000/health` for the backend health check.

## Logs & PIDs
- Runtime logs: `logs/backend.log`, `logs/frontend.log`.
- PID files: `pids/backend.pid`, `pids/frontend.pid`.
- These directories are already ignored by git (see `.gitignore`).
