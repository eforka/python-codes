import boto3

# print(dir(boto3))

s3 = boto3.client('s3')

print(dir(s3))

response = s3.list_buckets()
print(response)