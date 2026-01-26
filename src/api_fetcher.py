import os
import json
import boto3
import requests
from dotenv import load_dotenv
from logging_config import logging_configuration

# log_file = os.getenv("LOG_FILE_PATH") # Might need the log_file later in code

logger = logging_configuration()

try:
    logger.info("Testing 1,2,3!")
except AttributeError:
    print("There is a problem with your function!")