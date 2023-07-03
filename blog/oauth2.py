from typing import Annotated

from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from blog.database import get_db
from blog.jwt_token import verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_token(token, credentials_exception, db)
