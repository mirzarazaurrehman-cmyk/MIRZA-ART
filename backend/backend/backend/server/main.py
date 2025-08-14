from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import replicate
import os

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load API token from environment
REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")
if not REPLICATE_API_TOKEN:
    raise ValueError("REPLICATE_API_TOKEN not set in .env file")

# Create Replicate client
client = replicate.Client(api_token=REPLICATE_API_TOKEN)

@app.get("/")
def home():
    return {"message": "Backend is running"}

@app.post("/api/generate-video")
def generate_video(prompt: str = Query(..., description="Video prompt")):
    try:
        output = client.run(
            "lucataco/pixverse:8ac236e8f20ef149cd443b2014c6ff82f1cb962cb6e0181f1c1963cf86d1503e",
            input={
                "prompt": prompt,
                "num_frames": 24,
                "fps": 8,
                "width": 512,
                "height": 512
            }
        )
        return {"video_url": output}
    except Exception as e:
        return {"error": str(e)}
