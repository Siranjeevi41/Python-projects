import requests

def test_api_integration():
    # Assuming your Flask app is running locally on port 5000
    base_url = 'http://localhost:5000'
    
    # Simulate a file upload
    files = {'file': open('test_file.txt', 'rb')}
    response = requests.post(f'{base_url}/upload', files=files)
    
    # Add assertions to check if the response is as expected
    assert response.status_code == 200
    assert response.text == "File uploaded successfully."
