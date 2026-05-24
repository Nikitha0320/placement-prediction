# Placement Prediction

Lightweight placement prediction web app.

- Backend: FastAPI (see `backend/main_fast.py`)
- Frontend: React + Vite (see `frontend/`)

Prerequisites

- Python 3.11+ (for backend)
- Node.js 18+ and npm (for frontend)
- Docker (optional, recommended for production)

Quick local run (development)

1. Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate    # Windows
pip install -r requirements.txt
uvicorn main_fast:app --reload --host 127.0.0.1 --port 8000
```

2. Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend dev server (Vite) typically runs at `http://localhost:5173` and the backend at `http://127.0.0.1:8000`.

Docker (quick)

- Build and run both services with `docker-compose` (create files as needed):

```bash
docker-compose build
docker-compose up -d
```

Production notes

- Lock down CORS origins in `backend/main_fast.py` before production (replace `allow_origins=["*"]`).
- Use HTTPS via reverse proxy (nginx) or cloud provider.
- Ensure model artifacts in `backend/model/` are included in your Docker builds.

Deployment options

- Static frontend: Vercel, Netlify (connect repo and build).
- Full app: Render, Railway, Google Cloud Run, AWS App Runner — deploy backend as a web service and frontend as a static site or container.

Need me to:

- Add Dockerfiles and `docker-compose.yml` now, or
- Generate a one-click deploy manifest for Render/Cloud Run?

## Frontend Notes (Vite + React)

The frontend was scaffolded with Vite and uses React. The project includes a small template README explaining the Vite React template and available plugins.

Key points from the frontend template:

- The template includes support for `@vitejs/plugin-react` which uses Oxc and an alternative `@vitejs/plugin-react-swc` (SWC).
- The React Compiler is not enabled by default in the template; enabling it may affect build performance.
- For production apps, consider TypeScript and type-aware lint rules (see the Vite TS template for guidance).

Frontend quick commands

```bash
cd frontend
npm install
npm run dev   # development
npm run build # production build outputs to `dist`
```

If you want the original frontend template README preserved separately, I can keep `frontend/README.md`; I removed it to consolidate project documentation.
