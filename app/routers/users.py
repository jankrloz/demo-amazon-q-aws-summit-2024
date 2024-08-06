from datetime import datetime

from fastapi import APIRouter
from pydantic import BaseModel

from app.services.users import UserService

router = APIRouter(
    prefix="/users",
)


class UserDTO(BaseModel):
    name: str


@router.get("/")
async def get_users():
    user_service = UserService()
    users = user_service.get_users()
    return {"users": users}


@router.post("/")
async def create_user(user: UserDTO):
    user_service = UserService()
    user = user_service.create_user(user.name)
    return {"user": user}
