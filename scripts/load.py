import os
import boto3
from dotenv import load_dotenv

load_dotenv()

# S3 credentials
s3_access_key = os.getenv('ACCESS_KEY')
s3_secret_key = os.getenv('SECRET_KEY')


def save_dataframe_to_s3(dataframe, s3_bucket, s3_file_name):
    """
    Saves a Pandas DataFrame as a CSV file and uploads it to an S3 bucket.

    Args:
        dataframe (pd.DataFrame): The DataFrame to be saved.
        s3_bucket (str): The name of the S3 bucket.
        s3_file_name (str): The name of the file in the S3 bucket.
    """
    # Specify the path and name of the output CSV file
    output_file = 'local-file.csv'

    # Save the DataFrame as a CSV file locally
    dataframe.to_csv(output_file, index=False)
    # Configure AWS credentials
    session = boto3.Session(
        aws_access_key_id=s3_access_key,
        aws_secret_access_key=s3_secret_key
    )

    # Create an S3 client
    s3_client = session.client('s3')

    # Upload the file to the S3 bucket
    s3_client.upload_file(output_file, s3_bucket, s3_file_name)

    print('CSV file uploaded to S3 successfully')
