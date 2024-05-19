from pydantic import BaseModel, EmailStr

class UserSerializer(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    is_active: bool
    is_superuser: bool

    class Config:
        from_orm = True
        from_attributes=True