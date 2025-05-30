from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP,Text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Submission(Base):
    __tablename__="submission"
    submission_id=Column(String,nullable=False,primary_key=True)
    submission_title=Column(String,nullable=False)
    submission_url=Column(String,nullable=False)
    submission_time=Column(TIMESTAMP,nullable=False)
    submission_text=Column(Text,nullable=False)


