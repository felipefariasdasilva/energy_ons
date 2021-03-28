import pandas as pd
import boto3
from constants import *
from io import StringIO

def get_file():

    print(" >> get file from s3...")

    client = get_client()
    csv = get_csv_in_bucket(client)
    body = get_body_of(csv)
    
    return read_csv(body)


def get_client():
    return boto3.client(
                AWS_SERVICE, 
                aws_access_key_id = AWS_KEY_ACESS_ID,
                aws_secret_access_key = AWS_KEY_ACESS_SECRET,
            )

def get_csv_in_bucket(client):
    return client.get_object(
                Bucket = AWS_BUCKET_NAME, 
                Key = AWS_OBJECT_KEY
            )

def get_body_of(csv):
    return csv['Body'].read().decode(WINDOWS_1252_DECODE)

def read_csv(body):
    return pd.read_csv(StringIO(body))