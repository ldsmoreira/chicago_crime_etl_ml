import os
import boto3
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError

# Load environment variables from .env file
load_dotenv()

# Read credentials and settings from environment variables
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

def upload_to_s3(file_name, bucket, object_name=None):
    # Configure the boto3 client with credentials from .env
    s3 = boto3.client(
        's3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket, object_name)
        print(f"Successfully uploaded {file_name} to {bucket}/{object_name}")
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
    except NoCredentialsError:
        print("Credentials not available")


if __name__ == "__main__":

    file_name = "data/chicago_crimes_2020_to_2022.csv"
    bucket = AWS_BUCKET_NAME

    upload_to_s3(file_name, bucket, "data/chicago_crime_database/chicago_crime_csv/chicago_crimes_2020_to_2022.csv")
