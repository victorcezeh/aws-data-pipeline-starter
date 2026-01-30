from src.transformer import transform_data
from src.redshift_writer import write_to_redshift

def lambda_handler(event, context):
    # read api file from s3
    # load the file into lambda
    transformed = transform_data(data)
    write_to_redshift(transformed)