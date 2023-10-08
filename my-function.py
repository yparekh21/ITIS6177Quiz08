import json

YOUR_NAME = "Yash Parekh"

def lambda_handler(event, context):
    try:
        keyword = event['keyword']
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing "keyword" parameter in the request')
        }

    result = f"{YOUR_NAME} says {keyword}"
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
