from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from typing import List
from app.models import Story
from app.config import settings
import logging
from datetime import datetime
import pytz

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/top-stories", response_model=List[Story])
async def get_top_stories():
    try:
        response = requests.get(f"{settings.HACKERNEWS_API_URL}/newstories.json?print=pretty")
        if response.status_code != 200:
            logger.error(f"Failed to fetch top stories: {response.status_code}")
            raise HTTPException(status_code=500, detail="Failed to fetch data from HackerNews API")
        top_10_ids = response.json()[:10]
        
        stories = []
        for story_id in top_10_ids:
            story_res = requests.get(f"{settings.HACKERNEWS_API_URL}/item/{story_id}.json?print=pretty")
            if story_res.status_code != 200:
                logger.warning(f"Failed to fetch story {story_id}: {story_res.status_code}")
                continue
            story_data = story_res.json()
            ist_timezone = pytz.timezone('Asia/Kolkata')
            story_time = datetime.fromtimestamp(story_data['time'], ist_timezone).strftime('%Y-%m-%d %H:%M:%S')
            stories.append(Story(
                title=story_data['title'],
                author=story_data['by'],
                url=story_data.get('url', ''),
                score=story_data['score'],
                time=story_time
            ))
        return stories
    except requests.exceptions.RequestException as e:
        logger.error(f"HackerNews API is unreachable: {e}")
        raise HTTPException(status_code=500, detail="HackerNews API is unreachable")
