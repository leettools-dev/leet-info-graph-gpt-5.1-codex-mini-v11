#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="${LOG_DIR:-${SCRIPT_DIR}/logs}"
PID_DIR="${PID_DIR:-${SCRIPT_DIR}/pids}"
BACKEND_PORT="${BACKEND_PORT:-8000}"
FRONTEND_PORT="${FRONTEND_PORT:-3000}"

mkdir -p "${LOG_DIR}" "${PID_DIR}"

# Stop any previous runners so we can start cleanly
if [[ -x "${SCRIPT_DIR}/stop.sh" ]]; then
  "${SCRIPT_DIR}/stop.sh"
fi

# Start backend
BACKEND_LOG="${LOG_DIR}/backend.log"
BACKEND_PID_FILE="${PID_DIR}/backend.pid"

uvicorn backend.app.main:app --host 0.0.0.0 --port "${BACKEND_PORT}" >>"${BACKEND_LOG}" 2>&1 &
echo "$!" >"${BACKEND_PID_FILE}"

echo "Backend running on http://localhost:${BACKEND_PORT} (logs: ${BACKEND_LOG})"

# Start frontend
FRONTEND_LOG="${LOG_DIR}/frontend.log"
FRONTEND_PID_FILE="${PID_DIR}/frontend.pid"

npm --prefix frontend run dev -- --host 0.0.0.0 --port "${FRONTEND_PORT}" >>"${FRONTEND_LOG}" 2>&1 &
echo "$!" >"${FRONTEND_PID_FILE}"

echo "Frontend running on http://localhost:${FRONTEND_PORT} (logs: ${FRONTEND_LOG})"

# Final reminder
cat <<EOF
Services started successfully.
Backend: http://localhost:${BACKEND_PORT}
Frontend: http://localhost:${FRONTEND_PORT}
Logs: ${LOG_DIR}
PIDs: ${PID_DIR}
EOF
