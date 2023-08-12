import boto3

# Create a session using the configured AWS CLI credentials and specify the region
session = boto3.Session(region_name='us-east-1')  # Replace with your desired region

# Create a Secrets Manager client
secrets_manager = session.client('secretsmanager')

# Specify the secret name (SecretId) you want to retrieve
secret_name = 'siranjeevi'  # Replace with your SecretId

try:
    # Retrieve the secret value
    response = secrets_manager.get_secret_value(SecretId=secret_name)

    # Extract the secret value
    if 'SecretString' in response:
        secret_value = response['SecretString']
        print("Secret Value:", secret_value)
    else:
        print("Secret value not found.")
except Exception as e:
    print("An error occurred:", str(e))
