import boto3

# Let's use Amazon S3
s3 = boto3.client('s3')
buckets=s3.list_buckets()
mainBucket=[]
mainBucket=buckets['Buckets']
for bucket in mainBucket[0].values():
    print(bucket)

