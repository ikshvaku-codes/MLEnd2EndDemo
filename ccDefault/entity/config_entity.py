from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", 
                                 ["dataset_download_url", 
                                  "tgz_download_url", 
                                  "rar_data_dir", 
                                  "ingested_train_dir", 
                                  "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", 
                                 ["schema_file_path"])


# For feature Engineering
# processed_object_path:- Pickle object folder path
DataTransformationConfig = namedtuple("DataTransformationConfig", 
                                 [  "feature_1",
                                    "transformed_train_dir", 
                                    "transformed_test_dir", 
                                    "processed_object_path"])


ModelTrainerConfig = namedtuple("ModelTrainerConfig", 
                                 ["trained_model_file_path", 
                                  "base_accuracy"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
                                   ["model_evaluation_file_path",
                                    "time_stamp"])
PushModelConfig = namedtuple("PushModelConfig",
                             ["expoort_dir_path"])