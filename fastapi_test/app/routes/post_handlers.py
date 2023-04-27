# file: routes/post_handlers.py
# =============================================

import uuid
from uuid import UUID

from fastapi import APIRouter, HTTPException
from starlette import status

from app.models.models import Post
# =============================================

router = APIRouter()

MY_POST = [
  dict(
    id=UUID("64867f5b-ef55-4128-808f-77a55f6154b0"),
    title="title post 1",
    content="First post"
  ),
  dict(
    id=UUID("f89e5b43-a46d-43d6-b49c-897653b4a4da"),
    title="title post 2",
    content="Second post"
  ),
]
# =============================================

@router.get(path="/")
async def health_check() -> dict[str, str]:
  return { "Message": "Welcome to my health check!.." }

@router.post(path="/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
  # Generate a new UUID for the post ID
  post_id: UUID = uuid.uuid4()
  print(f"Generated UUID: {post_id}, type: {type(post_id)}")
  post.id = post_id

  post_to_dict = post.dict(
    exclude_none=True,
    exclude={
      "published": post.published is None,
      "rating": post.rating is None
    }
  )

  # Print the newly created post
  print(post)  # This will call the __str__ method of the Post class

  MY_POST.append(post_to_dict)
  return { "data": post_to_dict }

@router.get(path="/posts", status_code=status.HTTP_200_OK)
async def get_all_post():
  return { "data": MY_POST }

@router.get("/posts/{post_id}")
async def get_post_by_id(post_id: UUID):
  print(f"Searching for post_id: {post_id}")

  for post in MY_POST:
    # converts both UUID's to strings
    if str(post["id"]) == str(post_id):
      return { "post_details": post }

  raise HTTPException(
    status_code=404,
    detail=f"Post with ID {post_id} not found"
  )

@router.delete(path="/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(post_id: UUID):
  for index, post in enumerate(MY_POST):
    if str(post["id"]) == str(post_id):
      del MY_POST[index]
      return

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f"Post with ID {post_id} not found"
  )













