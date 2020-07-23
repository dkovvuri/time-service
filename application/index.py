import datetime
import json
import pytz

def handler(event,context):
    statusCode = 200
    path = event['path']
    if path == "/time":
        if "timezone" in event['queryStringParameters']:
            try: 
                timezone = event['queryStringParameters']['timezone']
                time = datetime.datetime.now(timezone).strftime("%d/%m/%Y %H:%M:%S")
                message = "Current Time in {} is {}".format(timezone,time)
                print(message)
            except TypeError:
                statusCode = 400
                message = "{} is not a valid timezone. Please use /timezones API to fetch a list of valid timezones.".format(timezone)
        else:
            time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            message = "Time in UTC is {}".format(time)
            print(message)
    elif path == "/timezones":
        message = json.dumps(pytz.common_timezones,indent=4)

    message = {
        'statusCode': statusCode,
        'body': message
    }

    return message