import requests
from datetime import datetime

# Step 1: API Response (Data)
api_url = 'https://jsonplaceholder.typicode.com/posts'
response = requests.get(api_url)
posts = response.json()

# Step 2: Extract Post Titles
titles = [post.get('title', '') for post in posts]

# Step 3: Remove Single Quotes
modified_titles = [title.replace("'", "") for title in titles]

# Step 4: Find the Age of a Post
current_date = datetime.now()
modified_posts = []

for post in posts:
    created_at = post.get('created_at', '')  # Get the 'created_at' value or an empty string if not present
    if created_at:
        created_at = datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%S.%fZ')  # Replace with the actual date property
        age_in_days = (current_date - created_at).days
        modified_posts.append({'title': post.get('title', ''), 'modified_title': post.get('title', '').replace("'", ""), 'age': age_in_days})


print(response.text)
print(modified_posts)
