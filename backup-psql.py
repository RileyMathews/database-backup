from sh import pg_dump
import gzip
import boto3
import os

# variables, change these to the names of things for your local project
local_file_name = 'backup.gz'
database_name = 'uploadtest'
s3_bucket_name = 'riley-mathews-database-backups'
s3_file_key = 'test/backup.gz'

with gzip.open(local_file_name, mode='wb') as file:
    # name of your database replaces 'uploadtest'
    pg_dump(database_name, _out=file)

    # initialize s3
    s3 = boto3.resource('s3')
    # name of your s3 bucket goes here!
    bucket = s3.Bucket(s3_bucket_name)

with gzip.open(local_file_name, mode='rb') as file:
    # key is the directory under the bucket you want your backup to live
    bucket.put_object(
        Key=s3_file_key,
        Body=file,
        ContentType='application/x-gzip',
        ContentEncoding='gzip',
    )

# os.remove('backup.gz')