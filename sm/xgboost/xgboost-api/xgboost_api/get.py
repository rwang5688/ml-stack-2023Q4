import sm_util
import json


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    
    # DEBUG: print event with formattings
    print("event: %s" % json.dumps(event, indent=2))

    # retrieve record
    record = ''
    if 'queryStringParameters' in event:
        query_string_parameters = event['queryStringParameters']
        print("query_string_parameters: %s" % (query_string_parameters))
        if 'record' in query_string_parameters:
            record = query_string_parameters['record']
    print("record: %s" % (record))

    # replace with your actual endpoint_name
    endpoint_name = 'xgboost-serverless-ep2023-09-01-05-44-56'
    print("endpoint_name: %s" % (endpoint_name))
    response = sm_util.invoke_endpoint(endpoint_name, record)
    print("response: %s" % json.dumps(response, indent=2))

    # set and log return_val
    return_val = {
        "statusCode": 200,
        "body": json.dumps(response)
    }
    print("return_val: %s" % json.dumps(return_val, indent=2))
    
    return return_val

