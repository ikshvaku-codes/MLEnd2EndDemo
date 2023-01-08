import sys, os, tarfile, zipfile, time
from ccDefault.entity.config_entity import DataIngestionConfig
from ccDefault.exception import CCDefaultException
from ccDefault.logger import logging
from ccDefault.entity.artifact_entity import DataIngestionArtifact
from six.moves import urllib
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np

"""
try:
            pass
        except Exception as e:
                    raise CCDefaultException(e,sys) from e
"""

class DataIngestion:
    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'>>'*20}Data ingestion log started.{'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CCDefaultException(e,sys) from e
    
    def download_data(self):
        try:
            #extracting remote URL to download dataset
            download_url = self.data_ingestion_config.dataset_download_url
            
            #folder location to download dataset
            tgz_download_dir = self.data_ingestion_config.tgz_download_url
            
            #check if folder exists if yes delete it
            if os.path.exists(tgz_download_dir):
                os.remove(tgz_download_dir)
            
            #create folder if not available
            os.makedirs(tgz_download_dir, exist_ok=True)
            
            #to get name of file from url
            ccDefault_file_name = os.path.basename(download_url)
            
            #Folder to store tgz file
            tgz_file_path = os.path.join(
                tgz_download_dir, 
                ccDefault_file_name
            )
            
            logging.info(f"Downloading files from :[{download_url}] into :[{tgz_file_path}]")

            
            #download file from given url and store in given folder
            urllib.request.urlretrieve(download_url, tgz_file_path)
            
            logging.info(f"Downloaded files from :[{download_url}] into :[{tgz_file_path}] successfully")
            return tgz_file_path
            
        except Exception as e:
                    raise CCDefaultException(e,sys) from e
    
    def extract_data(self, tgz_file_path:str):
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            #Check if compressed file exists
            if not os.path.exists(tgz_file_path):
                raise "File does not exist"
            
            #check if folder exists if yes delete it
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)
            
            #create folder if not available
            os.makedirs(raw_data_dir, exist_ok=True)
            
            logging.info(f"Extracting compressed files from :[{tgz_file_path}] into :[{raw_data_dir}]")

            if tgz_file_path.endswith(".zip"):
                with  zipfile.ZipFile(tgz_file_path,'r') as ccDefault_tgz_file_obj:
                    ccDefault_tgz_file_obj.extractall(path=raw_data_dir)
            else :
                
                with  tarfile.open(tgz_file_path) as ccDefault_tgz_file_obj:
                    ccDefault_tgz_file_obj.extractall(path=raw_data_dir)
            
            logging.info(f"Extracted compressed files from :[{tgz_file_path}] into :[{raw_data_dir}] successfully")

            
        except Exception as e:
                    raise CCDefaultException(e,sys) from e
    
    def split_test_train_data(self,) -> DataIngestionArtifact:
        try:
            raw_data_dir = self.data_ingestion_config.raw_data_dir
            
            file_name = os.listdir(raw_data_dir)[0]
            
            file_path = os.path.join(raw_data_dir, file_name)
            
            logging.info(f"Reading csv file: [{file_path}]")
            ccDefault_df = pd.read_csv(file_path)
              
            # ccDefault_df["income_cat"] = pd.cut(
            #     ccDefault_df["median_income"],
            #     bins=[0.0, 1.5, 3.0, 4.5, 6.0, np.inf],
            #     labels=[1,2,3,4,5]
            # )  
             
            logging.info(f"Splitting data into train and test")         
            strat_train_set = None
            strat_test_set = None
            
            split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
            
            for train_index, test_index in split.split(ccDefault_df, ccDefault_df["default.payment.next.month"]):
                strat_train_set = ccDefault_df.loc[train_index]
                strat_test_set = ccDefault_df.loc[test_index]           
            train_file_path = os.path.join(
                self.data_ingestion_config.ingested_train_dir,
                file_name
            )
            
            test_file_path = os.path.join(
                self.data_ingestion_config.ingested_test_dir,
                file_name
            )
            
            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_train_dir,exist_ok=True)
                logging.info(f"Exporting training datset to file: [{train_file_path}]")
                strat_train_set.to_csv(train_file_path, index=False)
                
            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.ingested_test_dir,exist_ok=True)
                logging.info(f"Exporting test dataset to file: [{test_file_path}]")
                strat_test_set.to_csv(test_file_path, index=False)
             
            data_ingestion_artifact = DataIngestionArtifact(
                                        train_file_path,
                                        test_file_path,
                                        True,
                                        f"Data ingestion completed successfully."
                                    )   
            logging.info(f"Data Ingestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact
        except Exception as e:
                    raise CCDefaultException(e,sys) from e 
    
    
    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try:
            tgz_file_path = self.download_data()
            time.sleep(5)
            self.extract_data(tgz_file_path)
            return self.split_test_train_data()
            
        except Exception as e:
                    raise CCDefaultException(e,sys) from e
                
                
    def __del__(self):
        logging.info(f"{'='*20}Data Ingestion Log Completed.{'='*20}")