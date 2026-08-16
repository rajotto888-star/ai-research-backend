import asyncio
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TopicRequest(BaseModel):
    topic: str

class ReportResponse(BaseModel):
    report: str

async def run_ai_research(topic: str) -> str:
    # TODO: Replace with your real AI call
    await asyncio.sleep(5)
    return f"Here is your research report on '{topic}':\n\nThis is a placeholder."

@app.post("/research", response_model=ReportResponse)
async def research(request: TopicRequest):
    topic = request.topic.strip()
    if not topic:
        raise HTTPException(status_code=400, detail="Topic cannot be empty")
    report = await run_ai_research(topic)
    return ReportResponse(report=report)

@app.get("/ping")
async def ping():
    return {"status": "ok", "timestamp": time.time()}
