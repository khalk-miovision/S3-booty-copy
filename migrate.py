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

credentials = response['Credentials']

s3 = boto3.resource(
    's3',
    aws_access_key_id=credentials['AccessKeyId'],
    aws_secret_access_key=credentials['SecretAccessKey'],
    aws_session_token=credentials['SessionToken'],
)
for bucket in s3.buckets.all():
    print(bucket.name)

# with open('copy_paths.csv') as csv_file:
#     logos = csv.reader(csv_file, delimiter=',')
#     for path in logos:
#         print(path[0])

sourceBucketName = ''
newPrefix = '/public/attachments/'
fileKey = ''

s3 = boto3.resource('s3')
copy_source = {
    'Bucket': sourceBucketName,
    'Key': fileKey
}
s3.meta.client.copy(copy_source, sourceBucketName, newPrefix + fileKey)
