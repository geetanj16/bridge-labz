import boto3

def delete_unused_volumes():

    ec2_client = boto3.client('ec2')


    response = ec2_client.describe_volumes()


    unused_volumes = [volume['VolumeId'] for volume in response['Volumes'] if not volume['Attachments']]


    for volume_id in unused_volumes:
        print(f"Deleting volume {volume_id}")
        ec2_client.delete_volume(VolumeId=volume_id)

if __name__ == "__main__":
    delete_unused_volumes()