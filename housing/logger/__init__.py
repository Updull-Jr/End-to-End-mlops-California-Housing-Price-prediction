import logging
from datetime import datetime
import os


LOG_DIR = "housing_logs"  #directory

CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

LOG_FILE_NAME = F"log_{CURRENT_TIME_STAMP}.log"

os.makedirs(LOG_DIR, exist_ok = True)  #CREATES THE DIRECTORY 

LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

logging.basicConfig(filename=LOG_FILE_PATH,
  filemode='w', #write ~ the mode to open the file
  format ='[%(asctime)s] %(name)s - %(levelname)s - %(message)s', 
  level = logging.INFO #set the root logger
  )