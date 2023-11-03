from graphene import ObjectType, List, String, Int, Schema
import requests

# Define a GraphQL type for User
class UserType(ObjectType):
    name = String()
    email = String()
    address = String()

# Define a GraphQL type for Post
class PostType(ObjectType):
    title = String()
    body = String()

# Define a query for the GraphQL server
class Query(ObjectType):
    # Endpoint 1: All users from villages "name 1" and "name 2"
    users_by_villages = List(UserType, villages=List(String))
    def resolve_users_by_villages(self, info, villages):
        # Implement logic to fetch users based on villages
        # You might need to replace the URL and adjust the logic based on your data source
        # For simplicity, assume you have a local data source with user information
        users = [
            {"name": "User1", "email": "user1@example.com", "address": "Village name 1"},
            {"name": "User2", "email": "user2@example.com", "address": "Village name 2"},
            # Add more user data as needed
        ]
        return [user for user in users if user['address'] in villages]

    # Endpoint 2: Number of users and user list from villages "name 1" and "name 2"
    users_summary_by_villages = List(UserType, villages=List(String))
    total_users = Int(villages=List(String))
    def resolve_users_summary_by_villages(self, info, villages):
        users = self.resolve_users_by_villages(info, villages)
        return users

    # Endpoint 3: All posts from 'jsonplaceholder.typicode.com/users'
    all_posts = List(PostType)
    def resolve_all_posts(self, info):
        # Make a request to fetch posts from the specified URL
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        posts = response.json()
        return posts

    # Endpoint 4: All posts and total number of posts from 'jsonplaceholder.typicode.com/posts'
    posts_summary = List(PostType)
    total_posts = Int()
    def resolve_posts_summary(self, info):
        posts = self.resolve_all_posts(info)
        return posts

    # Endpoint 5: Retrieve address & email from the response of https://jsonplaceholder.typicode.com/comments
    address_email_from_comments = List(UserType)
    def resolve_address_email_from_comments(self, info):
        response = requests.get('https://jsonplaceholder.typicode.com/comments')
        comments = response.json()
        # Extract unique addresses and emails from comments
        unique_addresses_emails = {comment['email']: comment['body'] for comment in comments}
        return [{"email": email, "address": address} for email, address in unique_addresses_emails.items()]

    # Endpoint 6: Retrieve unique addresses & emails from the response of https://jsonplaceholder.typicode.com/users
    unique_addresses_emails_from_users = List(UserType)
    def resolve_unique_addresses_emails_from_users(self, info):
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        users = response.json()
        # Extract unique addresses and emails from users
        unique_addresses_emails = {user['email']: user['address'] for user in users}
        return [{"email": email, "address": address} for email, address in unique_addresses_emails.items()]

# Create a GraphQL schema
schema = Schema(query=Query)
import json

# Test the GraphQL queries
result = schema.execute('''
{
  usersByVillages(villages: ["Village name 1", "Village name 2"]) {
    name
    email
    address
  }
  usersSummaryByVillages(villages: ["Village name 1", "Village name 2"]) {
    name
    email
    address
  }
  allPosts {
    title
    body
  }
  postsSummary {
    title
    body
  }
  addressEmailFromComments {
    email
    address
  }
  uniqueAddressesEmailsFromUsers {
    email
    address
  }
}
''')

# Extract data and errors
data = result.data
errors = result.errors

# Print the result
print("Data:", data)
print("Errors:", errors)

# Save the data to a JSON file
with open("village-1.json", "w") as json_file:
    json.dump(data, json_file)

