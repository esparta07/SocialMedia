from sqlalchemy.orm import Session
from typing import List, Optional
from domain.repository.post import PostRepository
from domain.entity.post import Post, Hashtag, PostCreate
from ......database import get_db

class PostRepositoryAdapter(PostRepository):
    def __init__(self, db: Session):
        self.db = db

    async def create_post(self, post: PostCreate, user_id: int) -> Post:
        db_post = Post(
            content=post.content,
            image=post.image,
            location=post.location,
            author_id=user_id
        )
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return db_post

    async def get_user_posts(self, user_id: int) -> List[Post]:
        return self.db.query(Post).filter(Post.author_id == user_id).all()

    async def get_posts_by_hashtag(self, hashtag_name: str) -> Optional[List[Post]]:
        hashtag = self.db.query(Hashtag).filter(Hashtag.name == hashtag_name).first()
        if not hashtag:
            return None
        return hashtag.posts

    async def get_random_posts(self, page: int, limit: int, hashtag: Optional[str] = None) -> List[Post]:
        query = self.db.query(Post)
        if hashtag:
            query = query.join(Hashtag).filter(Hashtag.name == hashtag)
        return query.offset((page - 1) * limit).limit(limit).all()

    async def get_post_by_id(self, post_id: int) -> Optional[Post]:
        return self.db.query(Post).filter(Post.id == post_id).first()

    async def delete_post(self, post_id: int) -> None:
        post = await self.get_post_by_id(post_id)
        self.db.delete(post)
        self.db.commit()

    async def like_post(self, post_id: int, username: str) -> bool:
        # Implement logic to like a post
        pass

    async def unlike_post(self, post_id: int, username: str) -> bool:
        # Implement logic to unlike a post
        pass

    async def get_liked_users(self, post_id: int) -> List[str]:
        post = await self.get_post_by_id(post_id)
        return [user.username for user in post.liked_by_users]
