import logging
import os
from datetime import datetime

#Create log dir to store logs
LOG_DIR = 'logs'
LOG_DIR = os.path.join(os.getcwd(), LOG_DIR)

# Creating log dir if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

# Creating filename based on the current timestamp
TIMESTAMP = f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"
file_name = f"(log_{TIMESTAMP}.log)"

# Creating filepath
log_file_path = os.path.join(LOG_DIR, file_name)

logging.basicConfig(
    filename=log_file_path,
    filemode='w',
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

