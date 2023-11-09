import requests
import pandas as pd

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


def get_users_information():
    print("Getting users informations...")

    query_users = requests.get(f"{BASE_URI}/users?size=100?is_json=true")

    query_json = query_users.json()

    user_list = []

    for user in query_json:

        user_random = {
            "ID": user.get("id"),
            "Nome": user.get("first_name"),
            "Sobrenome": user.get("last_name"),
            "Usuario": user.get("username"),
            "Email": user.get("email"),
            "Senha": user.get("password"),
            "Foto": user.get("avatar"),
            "Data de Nascimento": user.get("date_of_birth"),
            "Cartao de Credito": user.get("credit_card").get("cc_number"),
            "Cidade": user.get("address").get("city"),
            "Endereco": user.get("address").get("street_address"),
            "CEP": user.get("address").get("zip_code"),
            "Estado": user.get("address").get("state"),
            "Pais": user.get("address").get("country")

        }

        user_list.append(user_random)

    print("Done getting users informations.")

    return user_list


def insert_data_in_csv():
    try:
        user_information = get_users_information()

        df = pd.DataFrame(user_information)

        df.to_csv("users_informations.csv", index=False)

        print("CSV created")
    
    except Exception as err:
        print("Error: ", err)


def read_csv_pd():
    df = pd.read_excel('read_csv.csv')

    print(df.to_string()) 

insert_data_in_csv()
read_csv_pd()
