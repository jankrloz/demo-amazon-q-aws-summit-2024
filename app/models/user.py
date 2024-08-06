from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, Sequence, String
from sqlalchemy.orm import Mapped

from app.config.db import Base


class User(Base):
    __tablename__ = "users"

    id: int = Column(
        Integer, Sequence("user_id_seq"), primary_key=True, autoincrement=True
    )
    name: str = Column(String(50))
    birth_date: Mapped[datetime] = Column(DateTime, default="0000-00-00 00:00:00")

    def __repr__(self):
        return f"<User(name='{self.name}', birthdate='{self.birth_date}')>"
