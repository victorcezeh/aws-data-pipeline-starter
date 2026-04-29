import json
import boto3

def read_from_s3(event):
    s3 = boto3.client("s3")

    record = event["Records"][0]
    bucket = record["s3"]["bucket"]["name"]
    key = record["s3"]["object"]["key"]

    response = s3.get_object(Bucket=bucket, Key=key)
    data = json.loads(response["Body"].read())

    return data