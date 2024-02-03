from sqlalchemy import Column, Integer, String, DateTime
from base import Base
from sqlalchemy_utils import UUIDType
import datetime, uuid

class MediaUpload(Base):
    """ Media Upload """
    __tablename__ = 'media_uploads'
    id = Column(Integer, primary_key=True)
    mediaType = Column(String(250), nullable=False)
    fileSize = Column(Integer, nullable=False)
    uploadTimestamp = Column(DateTime, nullable=False)
    date_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    userID = Column(UUIDType, nullable=False, default=uuid.uuid4)
    trace_id = Column(UUIDType, nullable=False)
    def __init__(self, userID, mediaType, fileSize, uploadTimestamp, trace_id):
        self.mediaType = mediaType
        self.fileSize = fileSize
        self.uploadTimestamp = uploadTimestamp
        self.userID = userID
        self.trace_id = trace_id    
    def to_dict(self):
        return {
            'id': self.id,
            'mediaType': self.mediaType,
            'fileSize': self.fileSize,
            'uploadTimestamp': self.uploadTimestamp.isoformat(),
            'date_created': self.date_created.isoformat(),
            'userID': self.userID(),
            'trace_id': self.trace_id
        }