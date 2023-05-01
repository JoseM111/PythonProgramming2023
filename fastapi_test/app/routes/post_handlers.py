# file: routes/post_handlers.py
# =============================================
import logging
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

# CHECK COMMUNICATION #######################
@router.get(path="/")
async def health_check() -> dict[str, str]:
  return { "Message": "Welcome to my health check!.." }

# CREATE ####################################
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

# READ ######################################
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

# UPDATE ######################################
@router.put(path="/posts/{post_id}", status_code=status.HTTP_202_ACCEPTED)
async def update_post(post_id: UUID, post: Post):

  for (index, current_post) in enumerate(MY_POST):
    if str(current_post["id"]) == str(post_id):
      # Convert the stored_post dictionary to a Pydantic Post object
      current_post_obj = Post.parse_obj(current_post)
      # Create a dictionary from 'post', including only the fields that were
      # changed in the request. 'exclude_unset=True' means we ignore fields
      # that weren't given a new value in the update request.
      updated_fields_dict = post.dict(exclude_unset=True)

      # Merge the stored_post_obj dictionary and
      # updated_fields_dict using the double asterisk method
      updated_post_to_dict = {**current_post_obj.dict(), **updated_fields_dict}
      # Update the post in the MY_POST list
      MY_POST[index] = updated_post_to_dict

      # change back to an object to use the Post objects `__str__`
      updated_post_obj = Post.parse_obj(updated_post_to_dict)
      logging.info(msg=updated_post_obj)

      return {
        "message": f"Post with ID {post_id} has been updated",
        "updated_post": updated_post_to_dict
      }

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f"Post with ID {post_id} not found"
  )

# DELETE ######################################
@router.delete(path="/posts/{post_id}", status_code=status.HTTP_200_OK)
async def delete_post(post_id: UUID):
  for index, post in enumerate(MY_POST):
    if str(post["id"]) == str(post_id):
      # Remove and return item at index (default last).
      # Raises IndexError if list is empty or index is out of range.
      deleted_post = MY_POST.pop(index)

      # could have a status code of `204` Not Found but
      # using a status of `200` will display this message
      # when the item is successfully deleted
      response_success_msg = {
        "message": f"Post with ID {post_id} has been deleted",
        "deleted_post": deleted_post
      }

      return response_success_msg

  raise HTTPException(
    status_code=status.HTTP_404_NOT_FOUND,
    detail=f"Post with ID {post_id} not found"
  )













