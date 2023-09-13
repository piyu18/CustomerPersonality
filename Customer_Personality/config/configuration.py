import os, sys
from Customer_Personality.logger.logs import logging
from Customer_Personality.exception import CustomException
from Customer_Personality.utils.utils import read_yaml_file
from Customer_Personality.entity.config_entity import DataIngestionConfig
from Customer_Personality.constant import *

class AppConfiguration:
    def __init__(self, config_file_path:str = CONFIG_FILE_PATH):
        try:
            self.configs_info = read_yaml_file(file_path=config_file_path)
        except Exception as e:
            raise CustomException(e,sys)
        
    def get_data_ingestion(self): DataIngestionConfig

