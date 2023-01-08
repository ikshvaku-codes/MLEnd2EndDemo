from ccDefault.config.configuration import Configuration
from ccDefault.logger import logging
from ccDefault.exception import CCDefaultException
from ccDefault.entity.artifact_entity import DataIngestionArtifact
from ccDefault.entity.config_entity import DataIngestionConfig
from ccDefault.component.data_ingestion import DataIngestion
import sys,  os

"""
        try:
            pass
        except Exception as e:
                    raise CCDefaultException(e,sys) from e
"""


class Pipeline:
    def __init__(self,config: Configuration = Configuration()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise CCDefaultException(e,sys) from e

    def start_data_ingestion(self,):
        try:
            data_ingestion = DataIngestion(self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
                    raise CCDefaultException(e,sys) from e
                
    
    
    
    
    
    
    def run_pipeline(self,):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            
        except Exception as e:
                    raise CCDefaultException(e,sys) from e
