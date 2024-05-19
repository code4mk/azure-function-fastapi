from sqlalchemy import Boolean, Column, Integer, String
from fastapi_project.database.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    
    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}