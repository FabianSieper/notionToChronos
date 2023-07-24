from time import sleep
from notion_client import Client

from bin.generic_modules.notion_comparator import *

class GenericNotionConnector:

    def __init__(self, notion_api_key, database_url, database_name) -> None:

        self.notion_api_key = notion_api_key
        self.database_url = database_url
        self.database_name = database_name

        self.notion_client = Client(auth=self.notion_api_key)
        self.database_id = self.get_database_id()


    def create_notion_page(self, page):

            return self.notion_client.pages.create(parent={"database_id": self.database_id}, properties=page)


    def get_database_id(self):

        if self.database_url == None or self.database_name == None or self.notion_client == None:
            raise Exception("[ERROR] - At least one of the following does not seem to be initialized: database_url, database_name, notion_client")
        
        temp_database_id = ""

        amount_retries = 0
        successfully_searched_notion = False

        # Get all databases for the url provided
        while not successfully_searched_notion:
            try: 
                database_result = self.notion_client.search(filter={"property": "object", "value": "database"}, url=self.database_url).get("results")
                successfully_searched_notion = True

            except Exception:
                print("[INFO] - Failed to search Notion. Retrying. Amount of retries so far: " + str(amount_retries))
                sleep(1)
                amount_retries += 1

            # Get all names of found databases
        database_names = [result["title"][0]["plain_text"] for result in database_result]

        # Get Index of correct name
        database_index = database_names.index(self.database_name)

        if database_index == -1:
            print("[ERROR] - Could not find databse for name", self.database_name)
            exit()
        
        temp_database_id = database_result[database_index]["id"]
        
        return temp_database_id


    def build_notion_filter(property_name:str, property_type: str, comparator: NotionComperator, value: str):

        if comparator not in NotionComperator:
            raise ValueError(f"Invalid comparator: {comparator}")

        return {
            "property": property_name,
            property_type: {
                str(comparator): value
            }
        }


    def get_notion_pages(self, filter=None):
        all_pages = []
        start_cursor = None
        page_size = 100

        while True:
            if filter:
                results = self.notion_client.databases.query(database_id=self.database_id, filter=filter, start_cursor=start_cursor, page_size=page_size)

            else:
                results = self.notion_client.databases.query(database_id=self.database_id, start_cursor=start_cursor, page_size=page_size)

            all_pages.extend(results.get("results"))

            if "next_cursor" in results and results["next_cursor"]:
                start_cursor = results["next_cursor"]
            else:
                break

        return all_pages
