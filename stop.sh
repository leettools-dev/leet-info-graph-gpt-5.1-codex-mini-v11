#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_DIR="${PID_DIR:-${SCRIPT_DIR}/pids}"

if [[ -d "${PID_DIR}" ]]; then
  for pid_file in "${PID_DIR}"/*.pid; do
    if [[ -f "${pid_file}" ]]; then
      pid=$(cat "${pid_file}")
      if [[ -n "${pid}" ]] && kill -0 "${pid}" >/dev/null 2>&1; then
        kill "${pid}" || true
      fi
      rm -f "${pid_file}"
    fi
  done
fi
EOF