import os
import requests
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Get GitHub Token from environment
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# Set Authorization Header
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

# Send a GET request to GitHub API to fetch user info
response = requests.get("https://api.github.com/user", headers=headers)

# Check the response
if response.status_code == 200:
    user_data = response.json()
    print("✅ Successfully connected to GitHub!")
    print(f"Hello, {user_data['login']} 👋")
else:
    print("❌ Failed to connect. Status Code:", response.status_code)
