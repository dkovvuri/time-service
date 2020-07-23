import datetime
import json

def handler(event,context):
    print(json.dumps(event,skipkeys=True,indent=4))
    message = {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    return message