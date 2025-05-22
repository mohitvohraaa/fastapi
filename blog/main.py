from fastapi import FastAPI

from blog.routers import authentication
from . import models, database
from .routers import blog, user,authentication

app = FastAPI()
models.Base.metadata.create_all(bind=database.engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
