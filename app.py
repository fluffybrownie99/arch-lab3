import connexion, datetime, json, yaml, logging, logging.config
from connexion import NoContent
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from base import Base
from update_event_data import update_event_data
from media_upload import MediaUpload
from media_playback import MediaPlayback

with open('log_conf.yml', 'r') as f:
    log_config = yaml.safe_load(f.read())
    logging.config.dictConfig(log_config)
    
logger = logging.getLogger('basicLogger')
logger.setLevel(logging.DEBUG)

#Receiver DB Setup for credentials (Load info from app_conf.yml, add as dict, access values)
with open('app_conf.yml', 'r') as config_file:
    app_config = yaml.safe_load(config_file)
db_config = app_config['datastore']
db_user = db_config['user']
db_password = db_config['password']
db_hostname = db_config['hostname']
db_port = db_config.get('port', 3306)  # Provide a default port if not specified
db_name = db_config['db']

DB_ENGINE = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_hostname}:{db_port}/{db_name}')

# DB_ENGINE = create_engine('sqlite:///media_server.db')  # Connect to your SQLite database
Base.metadata.bind = DB_ENGINE
DB_SESSION = sessionmaker(bind=DB_ENGINE)

def media_upload(body):
    #this makes sure time is properly formatted for the database.
    upload_timestamp = datetime.datetime.strptime(body['uploadTimestamp'], '%Y-%m-%d %H:%M:%S')
    session = DB_SESSION()
    new_upload = MediaUpload(
        fileSize=body['fileSize'],
        mediaType=body['mediaType'],
        uploadTimestamp=upload_timestamp,
        userID=body['userID'],
        trace_id=body['trace_id']
    )
    session.add(new_upload)
    session.commit()
    response = {
        "mediaId": str(new_upload.id)
    }
    session.close()
    logger.info(f'Stored event "media_upload" request with a trace id of {body["trace_id"]}')
    #Cant return NoContent due to strict validation 
    return response.json(), response.status_code

def media_playback(body):
    session = DB_SESSION()
    playback_start_time = datetime.datetime.strptime(body['playbackStartTime'], '%Y-%m-%d %H:%M:%S')
    new_playback = MediaPlayback(
        mediaId=body['mediaId'],
        playbackStartTime=playback_start_time,
        userID=body['userID'],
        playbackId=body['playbackId'],
        playbackDuration=body.get('playbackDuration', None),
        trace_id=body['trace_id']
    )
    session.add(new_playback)
    session.commit()
    response = {
        "userID":str(new_playback.userID)
    }
    session.close()
    logger.info(f'Stored event "media_playback" request with a trace id of {body["trace_id"]}')
    return response.json(), response.status_code


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