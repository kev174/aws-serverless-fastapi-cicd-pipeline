from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Get Userssss!"}

@router.get("/kevin")
async def rootuserkevin():
    return {"message": "Get Kevin User"}