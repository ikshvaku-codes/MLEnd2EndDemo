from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig", 
                                 ["dataset_download_url", 
                                  "tgz_download_url", 
                                  "raw_data_dir", 
                                  "ingested_train_dir", 
                                  "ingested_test_dir"])

DataValidationConfig = namedtuple("DataValidationConfig", 
                                 ["schema_file_path",
                                  "report_file_path",
                                  "report_page_file_path"])


# For feature Engineering
# processed_object_path:- Pickle object folder path
DataTransformationConfig = namedtuple("DataTransformationConfig", 
                                 [  "feature_1",
                                    "transformed_train_dir", 
                                    "transformed_test_dir", 
                                    "processed_object_path"])


ModelTrainerConfig = namedtuple("ModelTrainerConfig", 
                                 ["trained_model_file_path", 
                                  "base_accuracy",
                                  "model_config_file_path"])

ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
                                   ["model_evaluation_file_path",
                                    "time_stamp"])
PushModelConfig = namedtuple("PushModelConfig",
                             ["expoort_dir_path"])
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", 
                                    ["artifact_dir"])