from src.s3_reader import read_from_s3
from src.transformer import transform_data
from src.redshift_writer import write_to_redshift
from src.logging_config import logging_configuration

logger = logging_configuration()

def process_handler(event, context):
    raw_data = read_from_s3(event)
    transformed = transform_data(raw_data)
    write_to_redshift(transformed)