from datetime import datetime, timedelta

from bin.generic_modules.generic_notion_connector import *
from bin.generic_modules.notion_comparator import *

class NotionConnector(GenericNotionConnector):

    def _add_days(self, date_string, add_days):

        date_format = "%Y-%m-%d"
        current_date = datetime.strptime(date_string, date_format)
        next_day = current_date + timedelta(days=add_days)

        return next_day.strftime(date_format)


    def get_pages_at_date(self, date_property_name: str, date: str):
        filter = {
            "and": [
                {
                    "property": date_property_name,
                    "date": {
                        str(NotionComperator.AFTER): self._add_days(date, -1)
                    }
                },
                {
                    "property": date_property_name,
                    "date": {
                        str(NotionComperator.BEFORE): self._add_days(date, 1)
                    }
                }
            ]
        }
        return self.get_notion_pages(filter=filter)
    