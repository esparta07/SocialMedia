from uuid import UUID
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class PostCreateDTO(BaseModel):
    content: str
    image: str
    location: str

class PostDTO(BaseModel):
    id: int
    content: str
    image: str
    location: str
    author_id: int
    likes_count: int
    created_dt: datetime  

class HashtagDTO(BaseModel):
    id: int
    name: str

class LikePostDTO(BaseModel):
    post_id: int
    username: str

class UnlikePostDTO(BaseModel):
    post_id: int
    username: str

class LikedUsersDTO(BaseModel):
    post_id: int
    liked_users: list
