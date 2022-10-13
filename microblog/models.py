from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from users.models import User
from core.db import Base

class Post(Base):
    __tablename__ = "microblog_posts"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    title = Column(String)
    text = Column(String(350))
    date = Column(DateTime)
    user = Column(Integer, ForeignKey("user.id"))
    user_id = relationship("User")
