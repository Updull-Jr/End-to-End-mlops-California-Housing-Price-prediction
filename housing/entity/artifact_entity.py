from collections import namedtuple

  #the output of the components

DataIngestionArtifact = namedtuple("DataIngestion", ["train_file_path", 
                                                      "test_file_path",
                                                      "is_ingested",
                                                      "message"])

DataValidationArtifact = namedtuple("DataValidationArtifact",
                                    ["schema_file_path", 
                                    "report_file_path", 
                                    "report_page_file_path", 
                                    "is_validated",
                                    "message"])



