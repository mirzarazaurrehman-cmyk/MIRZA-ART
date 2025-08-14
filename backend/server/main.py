from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import replicate

app = FastAPI()

# CORS Middleware (Frontend requests کو allow کرنے کے لیے)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variable سے API token لینا
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    raise ValueError("REPLICATE_API_TOKEN environment variable not set")

@app.get("/api/health")
async def health_check():
    return {"status": "ok"}

@app.post("/api/generate-video")
async def generate_video(prompt: str):
    try:
        output = replicate.run(
            "tencentarc/pixverse:latest",
            input={"prompt": prompt}
        )
        return {"video_url": output}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
