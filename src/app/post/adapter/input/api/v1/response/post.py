from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from src.app.auth.schemas import User

class PostResponse(BaseModel):
    id: int
    content: str
    image: Optional[str]
    location: Optional[str]
    created_at: datetime
    likes_count: int
    author_id: int

class UserResponse(BaseModel):
    username: str
    full_name: Optional[str]
    email: str

class PostListResponse(BaseModel):
    posts: List[PostResponse]

class UsersListResponse(BaseModel):
    users: List[UserResponse]
