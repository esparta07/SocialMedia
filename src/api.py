from fastapi import APIRouter
from src.app.auth.views import router as auth_router
# from src.app.post.views import router as post_router
from src.app.post.adapter.input.api.v1.post import router as post_router
from src.app.profile.views import router as profile_router
from src.app.activity.views import router as activity_router

router = APIRouter(prefix="/v1")

router.include_router(auth_router)
router.include_router(post_router)
router.include_router(profile_router)
router.include_router(activity_router)