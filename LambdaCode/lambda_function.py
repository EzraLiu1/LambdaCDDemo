import json
import datetime

def lambda_handler(event, context):

    curr_time = datetime.datetime.now()
    time_str = curr_time.strftime("%Y-%m-%d")

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "time": time_str,
                # "location": ip.text.replace("\n", "")
            }
        )
    }
