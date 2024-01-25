from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime

class MediaUpload(Base):
    """ Media Upload """
    __tablename__ = 'media_uploads'

    id = Column(Integer, primary_key=True)
    deviceId = Column(String(250), nullable=False)
    mediaType = Column(String(250), nullable=False)
    fileSize = Column(Integer, nullable=False)
    uploadTimestamp = Column(DateTime, nullable=False)
    date_created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __init__(self, deviceId, mediaType, fileSize, uploadTimestamp):
        self.deviceId = deviceId
        self.mediaType = mediaType
        self.fileSize = fileSize
        self.uploadTimestamp = uploadTimestamp
    
    def to_dict(self):
        return {
            'id': self.id,
            'deviceId': self.deviceId,
            'mediaType': self.mediaType,
            'fileSize': self.fileSize,
            'uploadTimestamp': self.uploadTimestamp.isoformat(),
            'date_created': self.date_created.isoformat()
        }