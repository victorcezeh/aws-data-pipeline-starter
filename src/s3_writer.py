import json
import boto3
from config import url, bucket_name, key
from api_fetcher import fetch_api_data
from logging_config import logging_configuration

logger = logging_configuration()
logger.info("Project begins!")


def write_to_s3(api_data):
    try:
        logger.info("Beginning API data loading to S3.....")

        s3 = boto3.client("s3")
        s3.put_object(
            Bucket=bucket_name, Key=key, Body=json.dumps(api_data).encode("UTF-8")
        )
        logger.info("API data loaded successfully into S3!")
    except Exception as e:
        logger.error(f"API data failed to load into S3: {e}")


data = fetch_api_data(url)
write_to_s3(data)
