from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from injector import inject

from src.app.post.container import post_container
from application.services.post import PostService
from request.post import PostCreateRequest
from response.post import PostResponse, UsersListResponse

router = APIRouter(prefix="/posts", tags=["posts"])

# Dependency for getting the database session
def get_db_session():
    return post_container.injector.provide(Session)

# Create an instance of PostService using dependency injection
post_service = post_container.injector.get(PostService)


@router.post("/", response_model=PostResponse, status_code=201)
@inject
async def create_post(
    post: PostCreateRequest,
    db: Session = Depends(get_db_session)
) -> PostResponse:
    return await post_service.create_post(post, db)


@router.get("/user", response_model=list[PostResponse])
@inject
async def get_current_user_posts(
    db: Session = Depends(get_db_session)
) -> list[PostResponse]:
    return await post_service.get_current_user_posts(db)


@router.get("/user/{username}", response_model=list[PostResponse])
@inject
async def get_user_posts(
    username: str,
    db: Session = Depends(get_db_session)
) -> list[PostResponse]:
    return await post_service.get_user_posts(username, db)


@router.get("/hashtag/{hashtag}", response_model=list[PostResponse])
@inject
async def get_posts_by_hashtag(
    hashtag: str,
    db: Session = Depends(get_db_session)
) -> list[PostResponse]:
    return await post_service.get_posts_by_hashtag(hashtag, db)


@router.get("/feed", response_model=list[PostResponse])
@inject
async def get_random_posts(
    page: int = 1,
    limit: int = 5,
    hashtag: str = None,
    db: Session = Depends(get_db_session)
) -> list[PostResponse]:
    return await post_service.get_random_posts(page, limit, hashtag, db)


@router.delete("/", status_code=204)
@inject
async def delete_post(
    post_id: int,
    db: Session = Depends(get_db_session)
) -> None:
    await post_service.delete_post(post_id, db)


@router.post("/like", status_code=204)
@inject
async def like_post(
    post_id: int,
    username: str,
    db: Session = Depends(get_db_session)
) -> None:
    await post_service.like_post(post_id, username, db)


@router.post("/unlike", status_code=204)
@inject
async def unlike_post(
    post_id: int,
    username: str,
    db: Session = Depends(get_db_session)
) -> None:
    await post_service.unlike_post(post_id, username, db)


@router.get("/likes/{post_id}", response_model=UsersListResponse)
@inject
async def users_like_post(
    post_id: int,
    db: Session = Depends(get_db_session)
) -> UsersListResponse:
    return await post_service.get_liked_users(post_id, db)


@router.get("/{post_id}", response_model=PostResponse)
@inject
async def get_post(
    post_id: int,
    db: Session = Depends(get_db_session)
) -> PostResponse:
    return await post_service.get_post(post_id, db)
