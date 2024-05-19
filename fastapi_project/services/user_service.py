from fastapi import HTTPException
from fastapi_project.database.database import SessionLocal
from fastapi_project.utils.base import the_sorting, paginate
from fastapi_project.models.users import User
from fastapi_project.schemas.user_schema import UserCreateSchema
from fastapi_project.serializers.user_serializer import UserSerializer

class UserService:
    def __init__(self):
        self.db = SessionLocal()
        
    def s_create_user(self, user: UserCreateSchema):
        db_user = self.db.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")
        new_user = User(**user.model_dump())
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        return new_user
      
    def s_get_users(self, request):
        users = self.db.query(User)
        users = the_sorting(request, users)
        return paginate(request, users, serilizer=UserSerializer, wrap='users')
      
    def s_get_user_by_id(self, user_id):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        return user
