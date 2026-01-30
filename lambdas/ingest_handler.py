from src.config import url
from src.s3_writer import write_to_s3
from src.api_fetcher import fetch_api_data
from src.logging_config import logging_configuration

logger = logging_configuration()

def ingest_handler(event, context):
    # Fetch data from API
    data = fetch_api_data(url)
    # Write raw data to S3
    write_to_s3(data)