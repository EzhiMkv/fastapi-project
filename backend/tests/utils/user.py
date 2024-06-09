from sqlalchemy.orm import Session

from db.repository.user import create_new_user
from schemas.user import UserCreate


def create_random_user(db: Session):
    user = UserCreate(email="testemail@pew.ru", password="12345")
    user = create_new_user(db=db, user=user)
    return user
