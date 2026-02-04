import boto3
from config import bucket_name

s3 = boto3.client("s3")

bucket_data = s3.list_buckets()
for bucket in bucket_data["Buckets"]:
   print(bucket)
   if not bucket:
      print("no bucket exists here!")

# def write_to_s3(api_data):
#    pass