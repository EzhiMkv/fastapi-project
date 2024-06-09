from sqlalchemy.orm import Session

from db.models.blog import Blog
from db.repository.blog import create_new_blog
from schemas.blog import CreateBlog
from tests.utils.user import create_random_user


def create_random_blog(db: Session) -> Blog:
    blog = CreateBlog(title="first blog", content="first blog content")
    user = create_random_user(db=db)
    blog = create_new_blog(blog=blog, db=db, author_id=user.id)
    return blog
