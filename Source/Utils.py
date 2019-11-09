# Miscallaenous useful code goes here
import boto3



# CAUTION: delete all your buckets in S3
s3 = boto3.resource('s3')

def Delete_All_Buckets(s3):
    for abucket in s3.buckets.all():
        bucket = s3.Bucket(abucket)
        for bucket_version in bucket.object_versions:
            bucket_version.delete()
        bucket.delete()


