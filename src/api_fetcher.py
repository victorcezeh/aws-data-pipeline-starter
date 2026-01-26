import os
import json
import boto3
import requests
from config import load_dotenv
from logging_config import logging_configuration

logger = logging_configuration()

try:
    logger.info("Testing 1,2,3!")
except AttributeError:
    print("There is a problem with your function!")