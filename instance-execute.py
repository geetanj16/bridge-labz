import boto3

ec2 = boto3.client('ec2')

# Replace with your actual values
vpc_id = 'vpc-0f102c5bd92945e75'  # Your VPC ID
public_subnet_id = 'subnet-03265733f3266d380'  # Public subnet ID
private_subnet_id = 'subnet-0887f220c5ce65725'  # Private subnet ID
public_ami_id = 'ami-08363bceaa8129056'  # Your public AMI ID
private_ami_id = 'ami-0fa28062762a4af9c'  # Your private AMI ID
instance_type = 't2.micro'  # Choose an appropriate instance type

# Security group creation (replace placeholder with desired name)
new_security_group_name = 'cli'
response = ec2.create_security_group(
    GroupName=new_security_group_name,
    Description='Security group for public and private instances',
    VpcId=vpc_id
)
new_security_group_id = response['GroupId']
# Define common parameters for both instances
common_params = {
    'InstanceType': instance_type,
    'MinCount': 1,
    'MaxCount': 1,
    'SecurityGroupIds': [new_security_group_id]  # Use the newly created group
}

# Launch public instance, set AMI and subnet accordingly
public_response = ec2.run_instances(
    SubnetId=public_subnet_id,
    ImageId=public_ami_id,
    **common_params
)
public_instance_id = public_response['Instances'][0]['InstanceId']

# Launch private instance, set AMI and subnet accordingly
private_response = ec2.run_instances(
    SubnetId=private_subnet_id,
    ImageId=private_ami_id,
    **common_params
)
private_instance_id = private_response['Instances'][0]['InstanceId']

print(f"Launched public instance with AMI {public_ami_id}: {public_instance_id}")
print(f"Launched private instance with AMI {private_ami_id}: {private_instance_id}")