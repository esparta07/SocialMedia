from typing import List, Optional
from ..entity.post import Post, Hashtag, PostCreate

class PostRepository:
    async def create_post(self, post: PostCreate, user_id: int) -> Post:
        raise NotImplementedError

    async def get_user_posts(self, user_id: int) -> List[Post]:
        raise NotImplementedError

    async def get_posts_by_hashtag(self, hashtag_name: str) -> Optional[List[Post]]:
        raise NotImplementedError

    async def get_random_posts(self, page: int, limit: int, hashtag: Optional[str] = None) -> List[Post]:
        raise NotImplementedError

    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        raise NotImplementedError

    async def delete_post(self, post_id: int) -> None:
        raise NotImplementedError

    async def like_post(self, post_id: int, username: str) -> bool:
        raise NotImplementedError

    async def unlike_post(self, post_id: int, username: str) -> bool:
        raise NotImplementedError

    async def get_liked_users(self, post_id: int) -> List[str]:
        raise NotImplementedError
