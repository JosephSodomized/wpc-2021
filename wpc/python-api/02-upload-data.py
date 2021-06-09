import boto3
from pprint import pprint as pp

s3 = boto3.resource('s3')
MY_BUCKET = '200532'

asci = '`---------------+---------------`'

bucket = s3.Bucket(MY_BUCKET)

bucket.put_object(
   Key="foo/moo/boo/zoo/hello.txt",
   Body=bytes(asci, 'utf-8'),
   ACL='private'
)