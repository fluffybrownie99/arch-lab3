from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy_utils import UUIDType
from base import Base
import datetime, uuid

class MediaPlayback(Base):
    """ Media Playback """
    __tablename__ = 'media_playbacks'
    id = Column(Integer, primary_key=True)
    mediaId = Column(String, nullable=False)
    playbackStartTime = Column(DateTime, nullable=False)
    userID = Column(UUIDType, nullable=False, default=uuid.uuid4)
    playbackId = Column(Integer, nullable=False)
    playbackDuration = Column(Integer)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    trace_id = Column(UUIDType, nullable=False)

    def __init__(self, mediaId, playbackStartTime, userID, playbackId, trace_id, playbackDuration=None):
        self.mediaId = mediaId
        self.playbackStartTime = playbackStartTime
        self.userID = userID
        self.playbackId = playbackId
        self.playbackDuration = playbackDuration
        self.trace_id = trace_id

    def to_dict(self):
        return {
            'id': self.id,
            'mediaId': self.mediaId,
            'playbackStartTime': self.playbackStartTime.isoformat(),
            'userID': self.userID,
            'playbackId': self.playbackId,
            'playbackDuration': self.playbackDuration,
            'date_created': self.date_created.isoformat(),
            'trace_id': self.trace_id
        }