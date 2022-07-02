from fastapi import APIRouter
from .endpoints import services, users, posts

router = APIRouter()

router.include_router(services.router, prefix="/test", tags=["Test"])
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(posts.router, prefix="/posts", tags=["Posts"])

