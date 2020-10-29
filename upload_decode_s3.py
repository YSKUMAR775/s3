import boto3


def fun_upload(file_path):

    file_name = file_path.split('/')[-1]

    ACCESS_KEY_ID = 'AKIAXB3Y4CS3GX34M5OS'
    ACCESS_SECRET_KEY = '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'
    AWS_DEFAULT_REGION = 'ap-south-1'
    BUCKET_NAME = 'kumar776'

    s3_res = boto3.resource(
        's3',
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=ACCESS_SECRET_KEY,
        region_name=AWS_DEFAULT_REGION,
        # config=Config(signature_version='s3v4')
    )
    my_bucket = s3_res.Bucket(BUCKET_NAME)

    obj = my_bucket.Object(key=file_name)
    response = obj.get()
    encoding = 'utf-8'
    lines = response['Body'].read().decode(encoding).split('\n')

    ####################(first method)#############

    # lines = response['Body'].read().split()
    # lines.pop()
    # print(lines)
    #
    # old_list = []
    # for i in lines:
    #     encoding = 'utf-8'
    #     x = i.decode(encoding)
    #
    #     old_list.append(x)

    ####################(second method)#############

    old_list = []
    for i in lines:
        a = i.strip()
        old_list.append(a)
    del old_list[0]  # we can use pop or del methods
    old_list.pop(-1)
    # print(old_list)

    new_list = []
    for i in old_list:
        x = i.split(',')
        # print(x)

        a = x[0].replace(' ', '_')
        b = x[1].replace(' ', '_')
        c = x[2].replace(' ', '_')
        d = x[3].replace(' ', '_')

        id = a
        period = b
        short_descriptions = c
        temperatures = d

        dict_data = {"id": id, "period": period, "short_descriptions": short_descriptions, "temperatures": temperatures}
        new_list.append(dict_data)

    return new_list


x = fun_upload('C:/Users/Hemanth Y/Desktop/weather.csv')
print(x)
