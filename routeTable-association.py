                                                                  
import boto3

ec2 = boto3.client('ec2')

# Replace with your values
public_route_table_id = 'rtb-0ef83a688c782f429'  # ID of the public route table
private_route_table_id = 'rtb-0a59d114a9ce450ca'  # ID of the private route table
internet_gateway_id = 'igw-03ad31de34b1efb67'
nat_gateway_id = 'nat-0c02103cc23c88a52'

# Public Route Table: Connect to Internet Gateway
ec2.create_route(
    RouteTableId=public_route_table_id,
    DestinationCidrBlock='0.0.0.0/0',  # Route all traffic to the internet
    GatewayId=internet_gateway_id
)

# Private Route Table: Connect to NAT Gateway
ec2.create_route(
    RouteTableId=private_route_table_id,
    DestinationCidrBlock='0.0.0.0/0',  # Route all traffic to the NAT gateway
    GatewayId=nat_gateway_id
)

print(f"Routes to internet gateway and NAT gateway created in respective route tables")
