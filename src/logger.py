import logging 
import os
from datetime import datetime
from config.path_config import PROJECT_ROOT


LOGS_DIR=PROJECT_ROOT+'/logs'
## Make dirs of logs relative which file is executed in which folder like main dir executed then it will 
# show in like src,logs and if file inside src folder then logs folder path will be src/logs and log file.
os.makedirs(LOGS_DIR,exist_ok=True)


LOG_FILE=os.path.join(LOGS_DIR,f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO)

def get_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger 
