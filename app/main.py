from fastapi import FastAPI

app = FastAPI(title="DocuMind API",
              description="An intelligent document management and AI knowledge platform",
              version="1.0.0")

@app.get("/")
def root():
    return {
        "message":"Welcome to DocuMind API"
    }

@app.get("/health")
def health_check():
    return {
        "status":"healthy"
    }