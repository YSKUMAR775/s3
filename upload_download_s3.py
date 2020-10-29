import boto3
import botocore
from botocore.client import Config


def upload_download():
    file_path = 'C:/Users/Hemanth Y/Desktop/Buddha.jpg'
    info = file_path.split('/')[-1]

    ###########(uploading the file)###########

    ACCESS_KEY_ID = 'AKIAXB3Y4CS3GX34M5OS'
    ACCESS_SECRET_KEY = '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'
    AWS_DEFAULT_REGION = 'ap-south-1'
    BUCKET_NAME = 'kumar775'

    # data = open('Buddha.jpg', 'rb')
    # data = open('C:/Users/Hemanth Y/Desktop/Buddha.jpg', "rb")
    # info = Path('C:/Users/Hemanth Y/Desktop/Ganesh.jpg')

    data = open(info, "rb")

    s3_res = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        # config=Config(signature_version='s3v4')               # first method here
    )
    s3_res.Bucket(BUCKET_NAME).put_object(Key=info, Body=data)

    my_config = Config(signature_version=botocore.UNSIGNED)     # second method
    # my_config = Config(signature_version='s3v4')              # we can also write first method

    ##############(downloading the file)###########

    s3_cli = boto3.client('s3', config=my_config)
    params = {"Bucket": BUCKET_NAME, "Key": info}
    final_url = s3_cli.generate_presigned_url('get_object', params)

    return {'url': final_url}


x = upload_download()
print(x)
