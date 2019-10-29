import boto3

client = boto3.client('sts')

token = str(input("Enter your token: "))

response = client.assume_role(
    RoleArn='OrganizationAccountAccessRole-Developer',
    RoleSessionName='@S3migration@',
    SerialNumber='arn:aws:iam::457774690605:mfa/sahmed',
    TokenCode=token
)

print(response)