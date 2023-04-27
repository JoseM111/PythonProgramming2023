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
    rating_str = '' if self.rating is None else f'rating: {self.rating}'
    published_str = '' if self.published is None else f'published: {self.published}'

    # Define a string with 6 spaces to use for indentation
    custom_spaces = f'\n{"":6}'

    # Conditionally add newline before published_str and rating_str
    published_str = '' if not published_str else f',{custom_spaces}{published_str}'
    rating_str = '' if not rating_str else f',{custom_spaces}{rating_str}'

    result = f"""post: {{
      id: {self.id},
      title: {self.title},
      content: {self.content}{published_str}{rating_str}
    }}""".replace('  ', ' ')  # Replace multiple spaces with a single space

    return result.strip()
# =============================================
