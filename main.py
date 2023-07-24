
from bin.init_project import get_user_info
from bin.init_project import NOTION_API_KEY_FIELD, NOTION_DATABASE_ID_FIELD, NOTION_DATABASE_NAME_FIELD

from bin.notion_connector import *
from bin.generic_modules.notion.notion_comparator import *

if __name__ == "__main__":
    
    user_info = get_user_info()
    notion = NotionConnector(
        user_info[NOTION_API_KEY_FIELD],
        user_info[NOTION_DATABASE_ID_FIELD],
        user_info[NOTION_DATABASE_NAME_FIELD]
        )

    notion_pages = notion._get_data_for_day("Start time", "2023-07-24", "Epic")
    