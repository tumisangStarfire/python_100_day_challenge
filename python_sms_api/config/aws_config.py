import boto3
import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

sms_client = boto3.client(
    service_name="sns",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_DEFAULT_REGION")
)

