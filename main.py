from scripts.transform import transform_data
from scripts.load import save_dataframe_to_s3
import uuid

# Create an example DataFrame
df = transform_data()

# Create tail of file_name
unique_id = str(uuid.uuid4())

# Specify the S3 bucket name and file name
bucket_name = 'demo-etl-bucket-se'
file_name = f'test_demo_csv_{unique_id}.csv'

# Call the function to save the DataFrame to S3


def main():
    try:
        save_dataframe_to_s3(df, bucket_name, file_name)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()


print('hello word')