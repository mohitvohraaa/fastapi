from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, models, database,token
from ..hashing import hash
from ..database import get_db

router = APIRouter(prefix="/login", tags=["Authentication"])

@router.post("/")
def login_user(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid credentials")
    
    if not hash.verify(request.password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    
     
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token":access_token, "token_type":"bearer"}

