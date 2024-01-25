import connexion
from connexion import NoContent

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
import datetime
import json
from update_event_data import update_event_data
from media_upload import MediaUpload
from media_playback import MediaPlayback


#Receiver 
DB_ENGINE = create_engine('sqlite:///media_server.db')  # Connect to your SQLite database
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

def media_upload(body, deviceId):
    session = DB_SESSION()
    new_upload = MediaUpload(
        deviceId=deviceId,
        fileSize=body['fileSize'],
        mediaType=body['mediaType'],
        uploadTimestamp=body['uploadTimestamp'],
    )
    session.add(new_upload)
    session.commit()
    session.close()
    return NoContent, 201

def media_playback(body, deviceId):
    session = DB_SESSION()
    new_playback = MediaPlayback(
        deviceId=deviceId,
        mediaId=body['mediaId'],
        playbackStartTime=body['playbackStartTime'],
        userID=body['userID'],
        playbackId=body['playbackId'],
        playbackDuration=body.get('playbackDuration', None),
        # Add other fields as necessary
    )
    session.add(new_playback)
    session.commit()
    session.close()
    return NoContent, 201



app = connexion.FlaskApp(__name__, specification_dir='')
#specification_dir is where to look for OpenAPI specifications. Empty string means
#look in the current directory
app.add_api("openapi.yaml",
            strict_validation=True,
            validate_responses=True)


#openapi.yaml is the name of the file
# strict_validation - whether to validate requests parameters or messages
# validate_responses - whether to validate the parameters in a request message against your OpenAPI specification


if __name__ == "__main__":
    app.run(port=8090)