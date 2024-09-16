from pydantic import BaseModel

class Story(BaseModel):
    title: str
    author: str
    url: str
    score: int
    time: str
