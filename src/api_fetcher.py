import logging
import requests
from config import url

logger = logging.getLogger(__name__)

try:
    logger.info("Data Platform Testing - 1,2,3!")
except AttributeError:
    logger.info("There is a problem with your function!")

def fetch_api_data(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        logger.info(f"Request Successful!: {response.status_code}")
        api_data = response.json()
        # print(type(api_data))
        # print(api_data)
        # first_record = api_data[0]
        # print(first_record)
        return api_data
    except requests.exceptions.HTTPError as e:
        logger.warning(f"HTTP ERROR: {e}")
    except requests.exceptions.RequestException as e:
        logger.warning(f"Request Failed! {e}")

# fetch_api_data(url)