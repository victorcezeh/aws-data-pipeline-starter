import os                                         # I know I will need this
import requests                                   # Already installed and I know I will need it
import boto3                                      # This is for interacting with AWS API
from dotenv import load_dotenv                    # I will need this to load env variables
from logging_config import logging_configuration # Importing log module

# log_file = os.getenv("LOG_FILE_PATH") # Might need the log_file later in code

logger = logging_configuration()

try:
    logger.info("Testing 1,2,3!")
except AttributeError:
    print("There is a problem with your function!")