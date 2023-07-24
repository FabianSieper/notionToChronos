
from bin.init_project import get_user_info
from bin.init_project import NOTION_API_KEY_FIELD, NOTION_DATABASE_URL_FIELD, NOTION_DATABASE_NAME_FIELD

from bin.notion_connector import *
from bin.generic_modules.notion_comparator import *

if __name__ == "__main__":
    
    user_info = get_user_info()
    notion = NotionConnector(
        user_info[NOTION_API_KEY_FIELD],
        user_info[NOTION_DATABASE_URL_FIELD],
        user_info[NOTION_DATABASE_NAME_FIELD]
        )

    notion_pages = notion.get_pages_at_date("Start time", "2023-07-24")
    
    print(notion_pages)
    print(len(notion_pages))