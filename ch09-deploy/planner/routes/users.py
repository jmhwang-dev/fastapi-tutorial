from fastapi import APIRouter, HTTPException, status, Depends
from models.users import User, TokenResponse
from database.connection import Database
from auth.hash_password import HashPassword
from typing import List
from beanie import PydanticObjectId
from fastapi.security import OAuth2PasswordRequestForm
from auth.jwt_handler import create_access_token

user_router = APIRouter(
    tags=["User",]
)
user_database = Database(User)
hash_password = HashPassword()

@user_router.post("/signup")
async def sign_new_user(user: User) -> dict:
    user_exist = await User.find_one(User.email == user.email)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    hashed_password = hash_password.create_hash(user.password)
    user.password = hashed_password
    await user_database.save(user)
    return {
        "message": "User successfully registered!"
    }

@user_router.post("/signin", response_model=TokenResponse)
async def sign_user_in(user: OAuth2PasswordRequestForm = Depends()) -> dict:
    user_exist = await User.find_one(User.email == user.username)

    if not user_exist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )
    if hash_password.verify_hash(user.password, user_exist.password):
        access_token = create_access_token(user_exist.email)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
    return {
        "message": "User signed in successfully."
    }

@user_router.delete("/{id}")
async def delete_user(id: PydanticObjectId) -> dict:
    user = await user_database.delete(id)
    if user:
        return {
            "message": "User deleted successfully."
        }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User with supplied ID does not exist"
    )

@user_router.get("/")
async def get_all_user() -> List[User]:
    all_user = await user_database.get_all()
    return all_user