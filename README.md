# leet-info-graph-gpt-5.1-codex-mini-v11

> This project is being developed by an autonomous coding agent.

## Overview

## Product Requirements Document (PRD)

**Product name (working):** Research Infographic Studio

---

### 1) Summary

Build a full-stack web application where users sign in with Google, submit researc...

## Features

- Dockerized architecture with FastAPI backend and Vite-powered React frontend, orchestrated via docker-compose for easy local or CI deployment.
- Quick start scripts (start.sh/stop.sh) that manage logs and PID files, plus documentation of required env vars for Google OAuth, OpenAI, and ports.
- Core schema definitions for articles, infographics, sources, and provenance ensure research results are structured for export and traceability.

## Getting Started

### Prerequisites

- Python 3.12
- Node.js 20
- Docker & Docker Compose

### Installation

```bash
./start.sh    # Run backend + frontend (backend on :8000, frontend on :3000)
docker compose up --build    # Containerized setup
```
# Installation instructions will be added
```

### Usage

```bash
# Frontend: http://localhost:3000
# Backend health check: http://localhost:8000/health
```
# Usage examples will be added
```

## Development

See `.leet/plans/` for the current development status.

## Testing

```bash
pytest backend/tests
npm --prefix frontend test
```
# Test instructions will be added
```

## License

MIT
