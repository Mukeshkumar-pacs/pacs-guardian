from fastapi import FastAPI

app = FastAPI(
    title="PACS Guardian",
    description="PACS and DICOM Monitoring Platform",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "application": "PACS Guardian",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

