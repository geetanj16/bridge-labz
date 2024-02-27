import boto3
from botocore.exceptions import ClientError

ec2_client=boto3.client('ec2',region_name='us-east-1')

try:
    response= ec2_client.create_db_snapshot(DBSnapshotIdentifier='rds-snapshot',
    DBInstanceIdentifier='database-1',
    Tags=[
        {
            'Key': 'rds',
            'Value': 'key'
        },
    ]
)
except ClientError as e:
    print(f"Error  creating snapshot:{e}")

    