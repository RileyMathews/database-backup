import boto3
import os

# variables
local_file_name = 'restore.gz'
database_name = 'uploadtest'
s3_bucket_name = 'riley-mathews-database-backups'
s3_file_key = 'test/backup.gz'

s3 = boto3.resource('s3')
bucket = s3.Bucket(s3_bucket_name)

bucket.download_file(s3_file_key, local_file_name)
