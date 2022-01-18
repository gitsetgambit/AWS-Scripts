import boto3

s3 = boto3.resource('s3',
                    aws_access_key_id='',
                    aws_secret_access_key=''
                    )
print("all the bucket names are:- ")
for bucket in s3.buckets.all():
    print(bucket.name, " ")
