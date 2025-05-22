from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, database,oauth2
from ..repositories import blog as blog_repo
from ..database import get_db

router = APIRouter(prefix="/blog", tags=["Blog"])


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_repo.create(request, db)

@router.get("/")
def get_all_blogs(db: Session = Depends(get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    return blog_repo.get_all(db)

@router.get("/{id}", response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    return blog_repo.get_by_id(id, db)

@router.delete("/{id}")
def delete_blog(id: int, db: Session = Depends(get_db)):
    return blog_repo.delete(id, db)

@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return blog_repo.update(id, request, db)
