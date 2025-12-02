from app.db_config import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Text


class User(Base):
    __tablename__ = 'user'

    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, unique=False, nullable=False)
    
    def __init__(self, username:str, password_hash:str):
        self.username = username
        self.password_hash = password_hash