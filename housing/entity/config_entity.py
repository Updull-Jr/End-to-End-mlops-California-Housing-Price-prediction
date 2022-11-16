  # the information we need to provide to the our ml pipeline

from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",
                                                    ["dataset_download_url", 
                                                    "tgz_download_dir", 
                                                    "raw_data_dir", 
                                                    "ingested_train_dir", 
                                                    "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", ["schema_file_path"])

DataTransformationConfig = namedtuple("DataTransformationConfig", ["add_bedroom_per_room",
                                                                   "transformed_train_dir", # where we save the transformed train_dataset
                                                                   "transformed_test_dir", #
                                                                   "preprocessed_object_file_path"]) #the feature eng. pickle_file


ModelTrainerConfig = namedtuple("ModelTrainerConfig", ["trained_model_file_path", "base_accuracy"]) 
                                                        #the pickle file location 


ModelEvaluationConfig = namedtuple("ModelEvaluationConfig", ["model_evaluation_file_path", "time_stamp"])

ModelPusherConfig = namedtuple("ModelPusherConfig", ["export_dir_path"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])

 


 

