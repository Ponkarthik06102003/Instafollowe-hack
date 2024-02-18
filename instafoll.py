import requests

# Replace this with the username of the Instagram account you want to check
instagram_username = ""

# Replace this with your Instagram API access token
access_token = "YOUR_ACCESS_TOKEN"

# Make a GET request to the Instagram API to retrieve the user's information
response = requests.get(f"https://api.instagram.com/v1/users/self/?access_token={access_token}")

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON to get the user's information
    user_data = response.json()["data"]

    # Check if the account is a business or professional account
    if user_data.get("is_business") or user_data.get("is_professional"):
        print(f"{instagram_username} is a business or professional account.")
    else:
        print(f"{instagram_username} is not a business or professional account.")

    # Check if the account is a private account
    if user_data.get("is_private"):
        print(f"{instagram_username} is a private account.")
    else:
        print(f"{instagram_username} is not a private account.")
else:
    print("Failed to retrieve user information.")
