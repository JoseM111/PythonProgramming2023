# file: routes/post_handlers.py
# =============================================

from fastapi import APIRouter, HTTPException
from app.models.models import Post
# =============================================

router = APIRouter()

MY_POST = [
  { "title": "title post 1", "content": "First post", "id": 1 },
  { "title": "title post 2", "content": "Second post", "id": 2 },
]
# =============================================

@router.get("/")
async def health_check() -> dict[str, str]:
  return { "Message": "Welcome to my health check!.." }

@router.post("/posts")
def create_post(post: Post):
  # increments the id when a new post is created
  post_id = len(MY_POST) + 1
  post.id = post_id

  post_to_dict = post.dict(
    exclude_none=True,
    exclude={
      'published': post.published is None,
      'rating': post.rating is None
    }
  )

  MY_POST.append(post_to_dict)
  return { "data": post_to_dict }

@router.get("/posts")
async def get_all_post():
  return { "data": MY_POST }

@router.get("/posts/{id}")
async def get_post(post_id: int):
  return { "post_details": f"Here is post {post_id}" }


# @router.get("/book-by-index/{index}")
# async def book_by_index(index: int) -> dict[str, str]:
#   if index < 0 or index >= len(BOOK_DB):
#     # FAIL
#     raise HTTPException(
#       status_code=404,
#       detail=f"Index {index} is out of range {len(BOOK_DB)}"
#     )
#   else:
#     return { "book": BOOK_DB[index] }
# =============================================















