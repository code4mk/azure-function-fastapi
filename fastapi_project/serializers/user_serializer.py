from pydantic import BaseModel, EmailStr

class UserSerializer(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_orm = True
        from_attributes=True