from sqlalchemy import Column, Integer, String
from data.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    status = Column(String)
    priority = Column(String)
    deadline = Column(String)