import boto3
import os

QUEQUE = os.getenv('QUEUE_URL')

sqs = boto3.resource('sqs')
queue = sqs.Queue(QUEUE_URL)

queue.send_message(
   MessageBody = "Hello world 1.0"
)