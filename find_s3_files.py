import boto3
from botocore.client import Config


def find_files():

    ACCESS_KEY_ID = 'AKIAXB3Y4CS3GX34M5OS'
    ACCESS_SECRET_KEY = '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'
    AWS_DEFAULT_REGION = 'ap-south-1'

    s3_client = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        config=Config(signature_version='s3v4')
    )

    BUCKET_NAME = 'kumar776'
    my_bucket = s3_client.Bucket(BUCKET_NAME)

    list_url = []
    for file in my_bucket.objects.all():
        a = file.key
        list_url.append(a)

    return list_url


x = find_files()
print(x)
