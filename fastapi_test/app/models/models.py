# file: models/models.py
# =============================================
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


# =============================================

class Post(BaseModel):
  id: Optional[UUID] = None
  title: str
  content: str
  published: Optional[bool] = None
  rating: Optional[int] = None

  def __str__(self) -> str:
    rating_str = f'rating: {self.rating}' if self.rating is not None else ''
    published_str = f'published: {self.published}' if self.published is not None else ''

    # Conditionally add newline before published_str and rating_str
    published_str = f'{published_str}' if published_str else ''
    rating_str = f'{rating_str}' if rating_str else ''

    result = f"""post: {{
           id: {self.id},
           title: {self.title},
           content: {self.content},
           {published_str},
           {rating_str}
        }}""".strip().replace('  ', ' ') # Replace multiple spaces with a single space

    return result
# =============================================
