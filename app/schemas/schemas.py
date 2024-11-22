from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str

class GroupCreate(GroupBase):
    created_by_id: int

class Group(GroupBase):
    id: int
    created_at: datetime
    members: List[User] = []

    class Config:
        orm_mode = True

class RoundBase(BaseModel):
    group_id: int
    paid_by_id: int
    amount: int
    notes: Optional[str] = None

class RoundCreate(RoundBase):
    pass

class Round(RoundBase):
    id: int
    date: datetime
    
    class Config:
        orm_mode = True
