from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..database.database import Base

# Association table for many-to-many relationship between users and groups
group_members = Table(
    "group_members",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("group_id", Integer, ForeignKey("groups.id"))
)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relationships
    groups = relationship("Group", secondary=group_members, back_populates="members")
    rounds_paid = relationship("Round", back_populates="paid_by")

class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    created_by_id = Column(Integer, ForeignKey("users.id"))
    
    # Relationships
    members = relationship("User", secondary=group_members, back_populates="groups")
    rounds = relationship("Round", back_populates="group")

class Round(Base):
    __tablename__ = "rounds"

    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"))
    paid_by_id = Column(Integer, ForeignKey("users.id"))
    amount = Column(Integer)  # Amount in cents
    date = Column(DateTime(timezone=True), server_default=func.now())
    notes = Column(String, nullable=True)
    
    # Relationships
    group = relationship("Group", back_populates="rounds")
    paid_by = relationship("User", back_populates="rounds_paid")
