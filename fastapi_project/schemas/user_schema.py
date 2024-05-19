from pydantic import BaseModel, EmailStr
from typing import Optional

# Pydantic model for creating a new user
class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


# Pydantic model for updating user data
class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
