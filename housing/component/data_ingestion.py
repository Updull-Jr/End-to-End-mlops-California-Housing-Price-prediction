from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataIngestionConfig
from housing.entity.artifact_entity import DataIngestionArtifact
import os,sys
import tarfile  #extract zip file
from six.moves import urllib #download file


class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config = data_ingestion_config

        except Exception as e:
            raise HousingException(e,sys) from e

    def download_housing_data(self,):
        try:
            #exctractremote url to download dataset
            downlod_url = self.data_ingestion_config.dataset_download_url

             #folder location to download the file
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            
             #the base name ~housing.tgz
            housing_file_name = os.path.basename(downlod_url)

            tgz_file_path = os.path.join(tgz_download_dir, housing_file_name)

            logging.info(f"downloading file from: [{downlod_url}] into [{tgz_file_path}]")
            urllib.request.urlretrieve(downlod_url, tgz_file_path)

            logging.info(f"file : [{tgz_file_path}] has been downloaded successfully.")
            return tgz_file_path

        except Exception as e:
            raise HousingException(e,sys) from e


    def extract_tgz_file(self):
        pass

    def split_data_as_train_test(self):
        pass

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
            




