import boto3

def create_s3_bucket(bucket_name, region='us-east-1'):
    try:
        # Initialize the S3 client
        s3_client = boto3.client('s3', region_name=region)

        # Create the S3 bucket
        if region == 'us-east-1':
            s3_client.create_bucket(
                Bucket=bucket_name
            )
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
        print(f"Bucket '{bucket_name}' created successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your-bucket-name' with your desired bucket name
bucket_name = 'boto3-bucket-new'

# Replace 'us-east-1' with your desired region
region = 'us-east-1'


# Call the function to create the S3 bucket
create_s3_bucket(bucket_name, region)