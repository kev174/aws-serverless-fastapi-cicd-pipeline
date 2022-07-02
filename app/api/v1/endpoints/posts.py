from fastapi import APIRouter

router = APIRouter()

# changed @app.get("/") to @router.get("/")
@router.get("/")
async def root():
    return {"message": "Posts endpoint: Get Posts!"}