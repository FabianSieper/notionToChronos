import os
import json

CONFIG_FILE_NAME="config.json"

# Config file keys
NOTION_API_KEY_FIELD = "notion_api_key"
NOTION_DATABASE_ID_FIELD = "notion_database_id"
NOTION_DATABASE_NAME_FIELD = "notion_database_name"
REQUIRED_CONFIG_FIELDS = [NOTION_API_KEY_FIELD, NOTION_DATABASE_ID_FIELD, NOTION_DATABASE_NAME_FIELD]

def get_user_info():

    user_data = {}

    if not os.path.exists(os.path.join(os.curdir, CONFIG_FILE_NAME)):

        with open(CONFIG_FILE_NAME, "w") as file:

            notion_api_key = input("Enter the Notion API key: ")
            database_id = input("Enter the database id, from which you would like to read time information: ")
            database_name = input("Enter the database name: ")

            user_data[NOTION_API_KEY_FIELD] = notion_api_key
            user_data[NOTION_DATABASE_ID_FIELD] = database_id
            user_data[NOTION_DATABASE_NAME_FIELD] = database_name

            json.dump(user_data, file)

    else:

        with open(CONFIG_FILE_NAME, "r") as file:
            user_data = json.load(file)
        
        if not all([field in user_data for field in REQUIRED_CONFIG_FIELDS]):
            raise Exception("Required keys were not found in config file. Required keys: " + ", ".join(REQUIRED_CONFIG_FIELDS))

    return user_data
