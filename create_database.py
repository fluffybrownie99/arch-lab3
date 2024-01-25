# create_database.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
import datetime

Base = declarative_base()

class MediaUpload(Base):
    __tablename__ = 'media_uploads'
    id = Column(Integer, primary_key=True)
    deviceId = Column(String)
    fileSize = Column(Integer)
    mediaType = Column(String)
    uploadTimestamp = Column(DateTime)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)

class MediaPlayback(Base):
    __tablename__ = 'media_playbacks'
    id = Column(Integer, primary_key=True)
    deviceId = Column(String)
    mediaId = Column(String)
    playbackStartTime = Column(DateTime)
    userID = Column(String)
    playbackId = Column(Integer)
    playbackDuration = Column(Integer)
    date_created = Column(DateTime, default=datetime.datetime.now())

if __name__ == '__main__':
    engine = create_engine('sqlite:///media_server.db')
    Base.metadata.create_all(engine)
