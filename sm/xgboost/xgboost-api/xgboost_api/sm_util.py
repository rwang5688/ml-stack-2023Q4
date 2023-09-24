import boto3
import json


def invoke_endpoint(endpoint_name, record):
    '''Call the sagemaker (serverless) inference endpoint
    '''
    print("invoke_endpoint: endpoint_name: %s." % (endpoint_name))
    print("invoke_endpoint: record: %s." % (record))

    client = boto3.client('sagemaker-runtime')
    
    # pyaload needs to be a byte stream so we need to encode the record
    payload = record.encode('utf-8')
    print("invoke_endpoint: payload's byte converted string is: %s, type: %s." % (str(payload), str(type(payload))))
    content_type = "text/csv"
    
    ie_response = client.invoke_endpoint(
        EndpointName=endpoint_name,
        Body=payload,
        ContentType=content_type
    )
    
    # ic_response['Body'] is a byte stream so we need to read and decode the streamt
    response = ie_response["Body"].read().decode("utf-8")
    print("invoke_endpoint: response: %s" % json.dumps(response, indent=2))

    return(response)

