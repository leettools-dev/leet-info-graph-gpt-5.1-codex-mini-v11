from fastapi import FastAPI

app = FastAPI(title="Research Infographic Studio Backend")

@app.get("/health")
async def health_check():
    return {"status": "ok"}
