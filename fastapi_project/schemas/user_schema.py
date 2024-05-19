from pydantic import BaseModel, EmailStr
from typing import Optional

# Pydantic model for creating a new user
class UserCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str


# Pydantic model for updating user data
class UserUpdateSchema(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
