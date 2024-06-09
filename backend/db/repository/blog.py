from sqlalchemy.orm import Session

from schemas.blog import CreateBlog, UpdateBlog
from db.models.blog import Blog


def create_new_blog(db: Session, blog: CreateBlog, author_id: int = 1) -> Blog:
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog


def retrieve_blog(db: Session, id: int) -> Blog:
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog


def list_blogs(db: Session):
    blogs = db.query(Blog).filter(Blog.is_active == True).all()
    return blogs


def update_blog(id: int, blog: UpdateBlog, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id).first()
    if not blog_in_db:
        return {"error": f"Блог с ID {id} не найден"}
    if not blog_in_db.author_id == author_id:  # new
        return {"error": "Только автор может изменить блог"}
    blog_in_db.title = blog.title
    blog_in_db.content = blog.content
    db.add(blog_in_db)
    db.commit()
    return blog_in_db


def delete_blog(id: int, author_id: int, db: Session):
    blog_in_db = db.query(Blog).filter(Blog.id == id)
    if not blog_in_db.first():
        return {"error": f"Блог с ID {id} не найден"}
    if not blog_in_db.author_id == author_id:  # new
        return {"error": "Только автор может удалить блог"}
    blog_in_db.delete()
    db.commit()
    return {"msg": f"Блог с ID {id} удален"}
