from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship
from sqlalchemy.orm import mapped_column

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    login: Mapped[str] = mapped_column(String(30), unique=True, index=True)
    password: Mapped[str]
    nickname: Mapped[Optional[str]]
    is_active: Mapped[bool] = mapped_column(default=True)


    def __repr__(self) -> str:
        return f'User {self.name} -> #{self.id}'


class Address(Base):
    __tablename__ = "address"

    id: Mapped[int] = mapped_column(primary_key=True)
    counry: Mapped[str]
    region: Mapped[str]
    street: Mapped[str] = mapped_column(default='вулиця І.Франка', nullable=True)


class Countries(Base):
    __tablename__ = 'countries'

    id: Mapped[int] = mapped_column(primary_key=True)
    index: Mapped[str] = mapped_column(String(5), nullable=True)
