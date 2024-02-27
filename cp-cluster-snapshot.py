                                                  
import boto3
from botocore.exceptions import ClientError

rds_client=boto3.client('rds',region_name='us-east-1')
try:
    response = rds_client.copy_db_cluster_snapshot(
    SourceDBClusterSnapshotIdentifier='database-1-final-snapshot',
    TargetDBClusterSnapshotIdentifier='copy-snapshot',
    Tags=[
        {
            'Key': 'snapshot',
            'Value': 'rds'
        },
    ],
    SourceRegion='us-west-2'
)
except ClientError as e:
    print(f"Error  creating snapshot:{e}")