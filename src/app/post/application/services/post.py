from typing import List, Optional
from domain.repository.post import PostRepository
from domain.entity.post import PostCreate, Post
from domain.services.post import AbstractPostService

class PostService(AbstractPostService):

    async def create_post(self, post: PostCreate, user_id: int) -> Post:
        return await self.repository.create_post(post, user_id)

    async def get_user_posts(self, user_id: int) -> List[Post]:
        return await self.repository.get_user_posts(user_id)

    async def get_posts_by_hashtag(self, hashtag_name: str) -> Optional[List[Post]]:
        return await self.repository.get_posts_by_hashtag(hashtag_name)

    async def get_random_posts(self, page: int, limit: int, hashtag: Optional[str] = None) -> List[Post]:
        return await self.repository.get_random_posts(page, limit, hashtag)

    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        return await self.repository.get_post_by_id(post_id)

    async def delete_post(self, post_id: int) -> None:
        await self.repository.delete_post(post_id)

    async def like_post(self, post_id: int, username: str) -> bool:
        return await self.repository.like_post(post_id, username)

    async def unlike_post(self, post_id: int, username: str) -> bool:
        return await self.repository.unlike_post(post_id, username)

    async def get_liked_users(self, post_id: int) -> List[str]:
        return await self.repository.get_liked_users(post_id)
