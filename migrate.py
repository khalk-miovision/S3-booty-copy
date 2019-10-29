import boto3
import csv


client = boto3.client('sts')

token = str(input("Enter your token: "))

response = client.assume_role(
    RoleArn='arn:aws:iam::751075880680:role/OrganizationAccountAccessRole-Developer',
    RoleSessionName='@S3migration@',
    SerialNumber='arn:aws:iam::457774690605:mfa/sahmed',
    TokenCode=token
)

s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

# with open('copy_paths.csv') as csv_file:
#     logos = csv.reader(csv_file, delimiter=',')
#     for path in logos:
#         print(path[0])