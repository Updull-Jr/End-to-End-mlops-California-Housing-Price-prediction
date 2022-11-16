# here we write all the initialied reuirements

import os

ROOT_DIR = os.getcwd() #to get our current working directory
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR, CONFIG_FILE_NAME)

from datetime import datetime


CURRENT_TIME_STAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%S')}"



  #Training Pipeline related variables
TRAINING_PIPELINE_CONFIG_KEY = "training_pipeline_config"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"


 #Data ingestion related variables
DATA_INGESTION_CONFIG_KEY = "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion" #the output i.e. train/test files
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
DATA_INGESTION_RAW_DATA_DIR_KEY = "raw_data_dir"
DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
DATA_INGESTION_INGESTED_DIR_NAME_KEY = "ingested_dir"
DATA_INGESTION_TRAIN_DIR_KEY = "ingested_train_dir"
DATA_INGESTION_TEST_DIR_KEY = "ingested_test_dir"


   #Data validation related variables
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
DATA_VALIADTION_ARTIFACT_DIR = "data_validation"
DATA_VALIADTION_SCHEMA_DIR = "config"
DATA_VALIDATION_SCHEMA_FILE_NAME = "schema.yaml"
DATA_VALIDATION_REPORT_PAGE_FILE_NAME = "report.html"