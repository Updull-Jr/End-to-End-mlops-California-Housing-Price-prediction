from collections import namedtuple

  #the output of the components

DataIngestionArtifact = namedtuple("DataIngestion", ["train_file_path", 
                                                      "test_file_path",
                                                      "is_ingested",
                                                      "message"])