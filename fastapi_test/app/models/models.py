# file: models/models.py
# =============================================

from pydantic import BaseModel
from app.types.types import ResultType
# =============================================

class Post(BaseModel):
  id: int = None
  title: str
  content: str
  published: ResultType[bool, None] = None
  rating: ResultType[int, None] = None

  def __str__(self) -> str:
    rating_str = f'rating: {self.rating}' if self.rating is not None else ''
    published_str = f'published: {self.published}' if self.published is not None else ''

    return f"""\npost: {{
       id: {self.id},
       title: {self.title},
       content: {self.content},
       {published_str}
       {rating_str}
    }}"""
# =============================================
