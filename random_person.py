import requests

# This is a study that you're making. It's to be based on BigDataCorp's company.
BASE_URI = "https://random-data-api.com/api/v2/"

# Use size=number to fetch an array of any resource.
# Use response_type=json to render JSON or response_type=xml to render XML.

# ENDPOINTS

# Users - /users
# Address - /addresses
# Banks - /banks
# Appliances - /appliances
# Beers - /beers
# Blood Types - /blood_types
# Credit Cards - /credit_cards

query_1_person = requests.get(f"{BASE_URI}/users?is_json=true")
query_json = query_1_person.json()

user_random = {
    "first_name": query_json["first_name"],
    "last_name": query_json["last_name"],
    "username": query_json["username"],
    "email": query_json["email"],
    "password": query_json["password"]
}

print(F"""
        ! INFO ABOUT THE USER ! 
        -----------------------
        [@] First Name: {user_random.get("first_name")}
        [@] Last Name: {user_random.get("last_name")}
        [@] Username: {user_random.get("username")}
        [@] Email: {user_random.get("email")}
        [@] Password: {user_random.get("password")}
""")
