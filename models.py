from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Column, Integer, String, BigInteger, Float


class Base(DeclarativeBase):
    pass


class UserProfile(Base):
    __tablename__ = 'user_profile'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = Column(BigInteger)
    user_lang: Mapped[str] = mapped_column()
    sex: Mapped[str] = Column(String)
    age: Mapped[int] = Column(Integer)
    height: Mapped[int] = Column(Integer)
    weight: Mapped[int] = Column(Integer)
    type_of_physical_activity: Mapped[str] = Column(String)
