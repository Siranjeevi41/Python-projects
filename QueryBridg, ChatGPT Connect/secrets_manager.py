import boto3
import base64
from botocore.exceptions import ClientError

def get_secret(secret_name):
    client = boto3.client('secretsmanager')
    try:
        response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in response:
            return response['SecretString']
        else:
            return base64.b64decode(response['SecretBinary']).decode('utf-8')
