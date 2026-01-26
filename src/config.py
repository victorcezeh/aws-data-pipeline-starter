import os
from dotenv import load_dotenv

load_dotenv()

aws_access_key=os.getenv("AWS_ACCESS_KEY")
aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
bucket_name=os.getenv("AWS_BUCKET_NAME")
bucket_region=os.getenv("AWS_BUCKET_REGION")
api_url=os.getenv("API_URL")
log_file=os.getenv("LOG_FILE_PATH")