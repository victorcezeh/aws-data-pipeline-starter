import os
import json
import boto3
import requests
from config import base_url, end_point
from logging_config import logging_configuration

logger = logging_configuration()
url = base_url + end_point

try:
    logger.info("Data Platform Testing - 1,2,3!")
except AttributeError:
    print("There is a problem with your function!")

def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        logger.info(f"Request Successful!: {response.status_code}")
        # simpsons_data = response.json()
        # print(simpsons_data) and then return simpsons_data later
    except requests.exceptions.HTTPError as e:
        logger.warning(f"HTTP ERROR: {e}")
    except requests.exceptions.RequestException as e:
        logger.warning(f"Request Failed! {e}")

fetch_api_data(url)