from app.config.db import Base, engine
from app.models.user import User

__all__ = ["User"]

Base.metadata.create_all(engine)
