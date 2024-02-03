# create_database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Uuid
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import UUIDType
import datetime, uuid

Base = declarative_base()

class MediaUpload(Base):
    __tablename__ = 'media_uploads'
    id = Column(Integer, primary_key=True)
    fileSize = Column(Integer)
    mediaType = Column(String)
    uploadTimestamp = Column(DateTime)
    userID = Column(Uuid)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    trace_id = Column(UUIDType, nullable=False)

class MediaPlayback(Base):
    __tablename__ = 'media_playbacks'
    id = Column(Integer, primary_key=True)
    mediaId = Column(String)
    playbackStartTime = Column(DateTime)
    userID = Column(Uuid)
    playbackId = Column(Integer)
    playbackDuration = Column(Integer)
    date_created = Column(DateTime, default=datetime.datetime.now())
    trace_id = Column(UUIDType, nullable=False)

if __name__ == '__main__':
    engine = create_engine('sqlite:///media_server.db')
    Base.metadata.create_all(engine)
