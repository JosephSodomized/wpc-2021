import json

def lambda_handler(order_request, context):
    
    
    if not 'photos' in order_request:
        raise Exception("invalid request, missing photos")
    
    if len(order_request['photos']) <= 1:
      raise Exception("not enought photos selected")
    
    return {
        'statusCode': 200,
        'body': "ok, your order was procesed"
    }
