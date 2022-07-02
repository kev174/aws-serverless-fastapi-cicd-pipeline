from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def testing_child_resource():
    return {"message": "services.py: Hi There! This is my service route endpoint."}