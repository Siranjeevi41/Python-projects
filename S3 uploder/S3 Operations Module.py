from flask import Flask, request
import boto3

app = Flask(__name__)

# S3 functions
def create_s3_bucket(bucket_name):
    s3_client = boto3.client('s3')
    
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        print(f"S3 Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating S3 Bucket: {e}")

def set_lifecycle_policy(bucket_name, policy_rules):
    s3_client = boto3.client('s3')
    
    try:
        s3_client.put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration={'Rules': policy_rules}
        )
        print(f"S3 Bucket '{bucket_name}' lifecycle policy set successfully.")
    except Exception as e:
        print(f"Error setting S3 Bucket lifecycle policy: {e}")

# Flask route for file upload
allowed_extensions = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        uploaded_file = request.files['file']

        if uploaded_file and allowed_file(uploaded_file.filename):
            # Valid file, process it
            # Implement code to handle successful file upload
            return "File uploaded successfully."
        else:
            # Invalid file
            return "Invalid file. Please upload a valid file."
    except Exception as e:
        # Implement code to handle failed file upload
        return f"Error uploading file: {e}"

if __name__ == '__main__':
    # Create S3 bucket and set lifecycle policy (replace with actual values)
    create_s3_bucket('your-bucket-name')
    set_lifecycle_policy('your-bucket-name', 'your-policy-rules')

    # Run Flask app
    app.run(debug=True)
