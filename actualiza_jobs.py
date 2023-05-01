import boto3

s3 = boto3.client('s3')
file_name = 'job_parcial2.py'

bucket_name = 'aws-glue-assets-497431091508-us-east-1'
file_path = f'scripts/{file_name}'
with open(file_name, 'rb') as f:
    s3.upload_fileobj(f, bucket_name, file_path)

file_name = 'job_parcial2_b.py'
file_path = f'scripts/{file_name}'
with open(file_name, 'rb') as f:
    s3.upload_fileobj(f, bucket_name, file_path)
