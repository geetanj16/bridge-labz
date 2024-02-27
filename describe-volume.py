import boto3
from botocore.exceptions import ClientError

def delete_unused_ebs_volumes(region_name):
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name=region_name)

    try:
        # Describe volumes not in use
        response = ec2_client.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])

        # Extract volume IDs
        volume_ids = []
        for volume in response['Volumes']:
            volume_ids.append(volume['VolumeId'])

        # Delete unused volumes
        if volume_ids:
            print("Deleting the following unused EBS volumes:")
            for volume_id in volume_ids:
                ec2_client.delete_volume(VolumeId=volume_id)
                print(f"Volume ID: {volume_id}")
        else:
            print("No unused EBS volumes found.")

    except ClientError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    region_name = input("Enter the AWS region name: ")
    delete_unused_ebs_volumes(region_name)
