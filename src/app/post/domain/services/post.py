# domain/services/post.py

from abc import ABC, abstractmethod
from typing import Optional, List
from domain.entity.post import PostCreate, Post
from domain.repository.post import PostRepository

class AbstractPostService(ABC):

    def __init__(self, repository: PostRepository):
        self.repository = repository

    @abstractmethod
    async def create_post(self, post: PostCreate, user_id: int) -> Post:
        pass

    @abstractmethod
    async def get_user_posts(self, user_id: int) -> List[Post]:
        pass

    @abstractmethod
    async def get_posts_by_hashtag(self, hashtag_name: str) -> Optional[List[Post]]:
        pass

    @abstractmethod
    async def get_random_posts(self, page: int, limit: int, hashtag: Optional[str] = None) -> List[Post]:
        pass

    @abstractmethod
    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        pass

    @abstractmethod
    async def delete_post(self, post_id: int) -> None:
        pass

    @abstractmethod
    async def like_post(self, post_id: int, username: str) -> bool:
        pass

    @abstractmethod
    async def unlike_post(self, post_id: int, username: str) -> bool:
        pass

    @abstractmethod
    async def get_liked_users(self, post_id: int) -> List[str]:
        pass
