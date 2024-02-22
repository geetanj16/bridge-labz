import boto3

ec2 = boto3.client('ec2')

# Replace with your VPC ID
vpc_id = 'vpc-0f102c5bd92945e75'

# Public Route Table
# Create the public route table
public_response = ec2.create_route_table(VpcId=vpc_id)
public_route_table_id = public_response['RouteTable']['RouteTableId']

# Add a route to the Internet Gateway (replace with your IGW ID)
igw_id = 'igw-03ad31de34b1efb67'
ec2.create_route(
    RouteTableId=public_route_table_id,
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=igw_id
)

# Private Route Table
# Create the private route table
private_response = ec2.create_route_table(VpcId=vpc_id)
private_route_table_id = private_response['RouteTable']['RouteTableId']

# Add a route to the NAT Gateway (replace with your NAT Gateway ID)
nat_gateway_id = 'nat-0bba863a03bca7eb6'
ec2.create_route(
        RouteTableId=public_route_table_id,
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=igw_id
)

# Private Route Table
# Create the private route table
private_response = ec2.create_route_table(VpcId=vpc_id)
private_route_table_id = private_response['RouteTable']['RouteTableId']
# Add a route to the NAT Gateway (replace with your NAT Gateway ID)
nat_gateway_id = 'nat-0bba863a03bca7eb6'
ec2.create_route(
    RouteTableId=private_route_table_id,
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId=nat_gateway_id
)

# Associate Public Subnets with Public Route Table
# Replace with your public subnet IDs
public_subnet_ids = ['subnet-03265733f3266d380', 'subnet-0ff1ee26db343bddc']

for subnet_id in public_subnet_ids:
    ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=public_route_table_id)

# Associate Private Subnets with Private Route Table
# Replace with your private subnet IDs
private_subnet_ids = ['subnet-0e9f1c42032fd0b5f', 'subnet-0887f220c5ce65725']

for subnet_id in private_subnet_ids:
    ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=private_route_table_id)

print(f"Public Route Table ID: {public_route_table_id}")
print(f"Private Route Table ID: {private_route_table_id}")