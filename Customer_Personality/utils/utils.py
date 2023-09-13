import os, sys
import yaml
from Customer_Personality.logger.logs import logging
from Customer_Personality.exception import CustomException


def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path, 'rb') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise CustomException(e, sys)