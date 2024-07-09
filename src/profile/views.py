from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from .schemas import Profile, FollowerList, FollowingList
from .service import get_followers_svc, get_following_svc, follow_svc, unfollow_svc, check_follow_svc,existing_user

from ..auth.service import get_current_user

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/users/{username}", response_class=Profile)
async def profile(username: str, db: Session= Depends(get_db)):
    db_user= await existing_user(db, username, "")
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid username"
        )
    profile = Profile.from_orm(db_user)
    return profile

@router.post("/follow{username}", status_code=status.HTTP_204_NO_CONTENT)
async def follow(username:str, token:str, db:Session = Depends(get_db)):
    db_user = await get_current_user(db, token)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid token"
        )
    res= await follow_svc(db, db_user.username, username)
    if res == False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="could not follow ")
    
@router.post("/unfollow{username}", status_code=status.HTTP_204_NO_CONTENT)
async def follow(username:str, token:str, db:Session = Depends(get_db)):
    db_user = await get_current_user(db, token)
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Invalid token"
        )
    res= await unfollow_svc(db, db_user.username, username)
    if res == False:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="could not follow ")
    

@router.get("/followers", response_model=FollowerList)
async def get_followers(token: str, db:Session = Depends(get_db)):
    current_user = await get_current_user(db, token)
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token"
        )
    return await get_followers_svc(db, current_user.id)

@router.get("/following", response_model=FollowerList)
async def get_followers(token: str, db:Session = Depends(get_db)):
    current_user = await get_current_user(db, token)
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid token"
        )
    return await get_following_svc(db, current_user.id)