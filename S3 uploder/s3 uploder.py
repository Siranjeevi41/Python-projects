import boto3

# Replace these with your actual AWS credentials
aws_access_key_id = 'AKIAS32HX6UZGYFTXSRG'
aws_secret_access_key = 'BAMyKpG16BsTl2rZ1LnwhBQTyQtkc8vjQK+Xyc5u'

# Create an S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# S3 functions
def create_s3_bucket(bucket_name):
    try:
        s3.create_bucket(Bucket=bucket_name)
        print(f"S3 Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating S3 Bucket: {e}")

# Specify the bucket name and object key
bucket_name = 'your-s3-bucket'  # Replace with your actual bucket name
object_key = 'example.txt'

# Create S3 bucket
create_s3_bucket(bucket_name)

# Upload a file to S3
local_file_path = r'C:\Users\siranjeevi\Dropbox\PC\Downloads\example.txt'  # Or use forward slashes
try:
    s3.upload_file(local_file_path, bucket_name, object_key)
    print(f"File uploaded to S3 bucket '{bucket_name}' with key '{object_key}'.")
except Exception as e:
    print(f"Error uploading file to S3: {e}")
