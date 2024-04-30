from sqlalchemy import create_engine
import logging
from sqlalchemy.orm import Session
from config import settings
from models import Base, UserProfile


class Database:
    def __init__(self, db_url: str):
        self.__db_url = db_url
        self.__engine = None

    def connect(self):
        self.__engine = create_engine(url=self.__db_url)
        try:
            Base.metadata.create_all(self.__engine)
            print("Connected to database")
        except Exception as e:
            logging.error(e)

    def create_user_profile(self, user_id, user_lang, sex, age, height, weight,
                            type_of_physical_activity):
        with Session(self.__engine, expire_on_commit=False) as session:
            user_profile = UserProfile(user_id=user_id, user_lang=user_lang, sex=sex, age=age, height=height,
                                       weight=weight, type_of_physical_activity=type_of_physical_activity)
            session.add(user_profile)
            session.commit()

    def get_user_profile(self, user_id):
        with Session(self.__engine, expire_on_commit=True, autocommit=False, autoflush=True) as session:
            user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
            return user_profile

    def update_user_profile(self, user_id, **kwargs):
        with Session(self.__engine, expire_on_commit=False) as session:
            user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
            if user_profile:
                for key, value in kwargs.items():
                    setattr(user_profile, key, value)
                session.commit()
            return user_profile

    def delete_user_profile(self, user_id):
        with Session(self.__engine, expire_on_commit=False) as session:
            user_profile = session.query(UserProfile).filter(UserProfile.user_id == user_id).first()
            if user_profile:
                session.delete(user_profile)
                session.commit()
                return True
            else:
                return False

db = Database(db_url=settings.db_url)
db.connect()
