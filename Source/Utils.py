# Miscallaenous useful code goes here
import boto3


# howto delete all your buckets in S3
s3 = boto3.resource('s3')

for abucket in s3.buckets.all():
    bucket = s3.Bucket(abucket)
    bucket.object_versions.delete()
    bucket.delete()
