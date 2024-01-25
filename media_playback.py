from sqlalchemy import Column, Integer, String, DateTime
from base import Base
import datetime

class MediaPlayback(Base):
    """ Media Playback """
    __tablename__ = 'media_playbacks'

    id = Column(Integer, primary_key=True)
    deviceId = Column(String, nullable=False)
    mediaId = Column(String, nullable=False)
    playbackStartTime = Column(DateTime, nullable=False)
    userID = Column(String, nullable=False)
    playbackId = Column(Integer, nullable=False)
    playbackDuration = Column(Integer)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, deviceId, mediaId, playbackStartTime, userID, playbackId, playbackDuration=None):
        self.deviceId = deviceId
        self.mediaId = mediaId
        self.playbackStartTime = playbackStartTime
        self.userID = userID
        self.playbackId = playbackId
        self.playbackDuration = playbackDuration

    def to_dict(self):
        return {
            'id': self.id,
            'deviceId': self.deviceId,
            'mediaId': self.mediaId,
            'playbackStartTime': self.playbackStartTime.isoformat(),
            'userID': self.userID,
            'playbackId': self.playbackId,
            'playbackDuration': self.playbackDuration,
            'date_created': self.date_created.isoformat()
        }