from scripts.transform import transform_data
from scripts.load import save_dataframe_to_s3

# Create an example DataFrame
df = transform_data()

# Specify the S3 bucket name and file name
bucket_name = 'demo-etl-bucket-se'
file_name = 'test_demo_csv.csv'

# Call the function to save the DataFrame to S3
save_dataframe_to_s3(df, bucket_name, file_name)
