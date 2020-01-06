import logging
import os
from datetime import datetime

import boto3

bucket = path = os.getenv("bucket", "botopush-example")

def handle(event, context):
    logging.info(str(event.body, encoding="utf-8"))

    timestamp = datetime.utcnow().isoformat()
    key = f"{timestamp}-trafficmock-request.json"

    boto3.client("s3").put_object(Body=event.body, Bucket=bucket, Key=key)

    return {
        "statusCode": 200,
        "body": "Hello from OpenFaaS!"
    }
