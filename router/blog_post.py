from typing import Optional, List, Dict

from fastapi import APIRouter, Query, Body, Path
from pydantic import BaseModel

router = APIRouter(
    prefix="/blog",
    tags=["blog"],
)


class Image(BaseModel):
    url: str
    alias: str


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: str
    published: Optional[bool]
    tags: List[str] = []
    metadata: Dict[str, str] = {"key": "val1"}
    image: Optional[Image] = None


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {"id": id, "data": blog, "version": version}


@router.post("/new/{id}/comment/{comment_id}")
def create_comment(
    blog: BlogModel,
    id: int,
    comment_title: int = Query(
        None,
        title="Title of the comment",
        description="some description of comment title",
        alias="comment Title",
        deprecated=True,
    ),
    content: str = Body(..., min_length=4, max_length=10, regex="^[a-z\s]*$"),
    v: Optional[List[str]] = Query(["1.0", "2.0", "3.0"]),
    comment_id: int = Path(None, gt=5, le=10),
):
    return {
        "blog": blog,
        "id": id,
        "comment_title": comment_title,
        "content": content,
        "version": v,
        "comment_id": comment_id,
    }


def required_functionality():
    return {"message": "learning fastapi is important"}
