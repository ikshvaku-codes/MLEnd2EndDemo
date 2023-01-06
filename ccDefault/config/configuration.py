from ccDefault.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelTrainerConfig, PushModelConfig, TrainingPipelineConfig
from ccDefault.constants import *
from ccDefault.util import read_yaml
from ccDefault.exception import CCDefaultException
from ccDefault.logger import logging
import sys

class Configuration:
    def __init__(self,
                 config_file_path:str=CONFIG_FILE_PATH,
                 current_time_stamp:str=CURRENT_TIME_STAMP) -> None:
        try:
            self.config_info = read_yaml(config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise CCDefaultException(e,sys) from e
        
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            
            artifect_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(
                artifect_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )

            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            
            tgz_download_url = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )
            
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY]
            )
            
            ingested_train_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            
            ingested_test_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )
            data_ingestion_config = DataIngestionConfig(dataset_download_url, 
                                                        tgz_download_url, 
                                                        raw_data_dir, 
                                                        ingested_train_dir, 
                                                        ingested_test_dir)
            logging.info(f"Training pipeline config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise CCDefaultException(e,sys) from e
    
    def get_data_validation_config(self) -> DataValidationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_valid_artifact_dir = os.path.join(
                artifact_dir,
                DATA_VALIDATION_ARTIFACT_DIR_NAME,
                self.time_stamp
            )
            
            data_valid_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            schema_file_path = os.path.join(
                data_valid_artifact_dir,
                data_valid_info[DATA_VALIDATION_SCHEMA_DIR_KEY],
                data_valid_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]
            )
            report_file_path = os.path.join(
                data_valid_artifact_dir,
                data_valid_info[DATA_VALIDATION_REPORT_FILE_NAME_KEY]
            )
            report_page_file_path = os.path.join(
                data_valid_artifact_dir,
                data_valid_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY]
            )
            data_valid_config = DataValidationConfig(
                schema_file_path,
                report_file_path,
                report_page_file_path
            )
            logging.info(f"Data Validation config: {data_valid_config}")
            return data_valid_config
        except Exception as e:
            raise CCDefaultException(e,sys) from e
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            data_trans_dir = os.path.join(
                artifact_dir,
                DATA_TRANSFORMATION_ARTIFACT_DIR,
                self.time_stamp
            )
            
            data_trans_info = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            
            feature_1 = data_trans_info[DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY]
            
            transformed_train_dir = os.path.join(
                data_trans_dir,
                data_trans_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
                data_trans_info[DATA_TRANSFORMATION_TRAIN_DIR_NAME_KEY]
            )
            
            transformed_test_dir =  os.path.join(
                data_trans_dir,
                data_trans_info[DATA_TRANSFORMATION_DIR_NAME_KEY],
                data_trans_info[DATA_TRANSFORMATION_TEST_DIR_NAME_KEY]
            )
            
            processed_object_path =  os.path.join(
                data_trans_dir,
                data_trans_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY],
                data_trans_info[DATA_TRANSFORMATION_PREPROCESSED_FILE_NAME_KEY]
            )
            
            data_trans_config = DataTransformationConfig(
                feature_1,
                transformed_train_dir,
                transformed_test_dir,
                processed_object_path
            )
            logging.info(f"Data Transformation config: {data_trans_config}")

            return data_trans_config
        except Exception as e:
            raise CCDefaultException(e,sys) from e
        
        
    def get_model_trainer_config(self)-> ModelTrainerConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_train_dir = os.path.join(
                artifact_dir,
                MODEL_TRAINER_ARTIFACT_DIR,
                self.time_stamp
            )
            
            model_train_info = self.config_info[MODEL_TRAINER_CONFIG_KEY]
            
            trained_model_file_path = os.join.path(
                model_train_dir,
                model_train_info[MODEL_TRAINER_TRAINED_MODEL_DIR_KEY],
                model_train_info[MODEL_TRAINER_TRAINED_MODEL_FILE_NAME_KEY]
            )
            
            base_accuracy = model_train_info[MODEL_TRAINER_BASE_ACCURACY_KEY]
            
            model_config_file_path = os.path.join(
                model_train_dir,
                model_train_info[MODEL_TRAINER_MODEL_CONFIG_DIR_KEY],
                model_train_info[MODEL_TRAINER_MODEL_CONFIG_FILE_NAME_KEY]
            )
            
            model_trainer_config = ModelTrainerConfig(
                trained_model_file_path,
                base_accuracy,
                model_config_file_path
            )
            logging.info(f"Model Trainer config: {model_trainer_config}")

            return model_trainer_config
        except Exception as e:
            raise CCDefaultException(e,sys) from e   
    
    def get_model_evalution_config(self) -> ModelEvaluationConfig:
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_val_dir = os.path.join(
                artifact_dir,
                MODEL_EVALUATION_ARTIFACT_DIR,
                self.time_stamp
            )
            
            model_val_info = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            model_evaluation_file_path = os.path.join(
                model_val_dir,
                model_val_info[MODEL_EVALUATION_FILE_NAME_KEY]
            )
            model_eval_config = ModelEvaluationConfig(
                model_evaluation_file_path,
                self.time_stamp
            )
            logging.info(f"Model Evalution config: {model_eval_config}")
            return model_eval_config
        except Exception as e:
            raise CCDefaultException(e,sys) from e      
    
    def get_model_pusher_config(self) -> PushModelConfig:
        try:
            
            
            
            model_push_info = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            
            expoort_dir_path = os.path.join(
                ROOT_DIR,
                model_push_info[MODEL_PUSHER_MODEL_EXPORT_DIR_KEY],
                self.time_stamp
            )
            
            model_push_config = PushModelConfig(
                expoort_dir_path
            )
            logging.info(f"Model Evalution config: {model_push_config}")
            return model_push_config
        except Exception as e:
            raise CCDefaultException(e,sys) from e      
    
    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
                                         training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                         training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]) 
            training_pipeline_config = TrainingPipelineConfig(artifact_dir = artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise CCDefaultException(e,sys)
    
    