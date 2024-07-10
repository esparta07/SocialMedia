from pydantic import BaseModel

class PostCreateRequest(BaseModel):
    content: str
    image: str = None
    location: str = None

class PostUpdateRequest(BaseModel):
    content: str
    image: str = None
    location: str = None

class PostLikeRequest(BaseModel):
    username: str
