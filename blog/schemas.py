from pydantic import BaseModel

# ------------------ Blog Input Schema ------------------
class Blog(BaseModel):
    title: str
    body: str
    class Config:
        orm_mode = True


# ------------------ User Input Schema ------------------
class User(BaseModel):
    name: str
    email: str
    password: str

# ------------------ User Output Schema ------------------
class ShowUser(BaseModel):
    name: str
    email: str
    blogs:list[Blog]=[]
    class Config:
        orm_mode = True

# ------------------ Blog Output Schema ------------------
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    class Config:
        orm_mode = True
 

class Login(BaseModel):
    email:str
    password:str

    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
