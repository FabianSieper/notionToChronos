
from bin.generic_modules.notion.generic_notion_connector import *
from bin.generic_modules.notion.notion_comparator import *

import pandas as pd

class NotionConnector(GenericNotionConnector):

    DURATION_COLUMN = "Duration (h)"

    # Get data for a specific day and extract important information from it
    def _get_data_for_day(self, date_property_name: str, date: str, group_by: str):
        
        if date_property_name is None or date is None or group_by is None:
            raise ValueError("[ERROR] - At least one of the following parameters is missing: date_property_name, date, group_by")
        
        data = self.get_property_values_for_date(date_property_name=date_property_name, date=date)
        
        print("[INFO] - Processing data ...")

        # Group time-entries by epic and sum them
        data_df = pd.DataFrame(data)
        data_df = data_df[[group_by, self.DURATION_COLUMN]]

        # TODO: epics are not found for some reason, even though they are in teh notion database
        data_df['Epic'] = data_df['Epic'].apply(self._extract_epic_from_json)
        data_df[self.DURATION_COLUMN] = data_df[self.DURATION_COLUMN].apply(self._extract_duration_from_json)
        
        print(data_df)
        
        # Sum up the duration values based on column group_by
        data_grouped = data_df.groupby(group_by).sum()

        print(data_grouped)

        # TODO: return something
        

    # Extracting the the first epic of the epic-json-object
    def _extract_epic_from_json(self, row):
        if row and 'rollup' in row and 'array' in row['rollup'] and len(row['rollup']['array']) > 0:
            return row['rollup']['array'][0]
        return None


    # Extracting the duration of the duration-json-object
    def _extract_duration_from_json(self, row):
        if row and 'formula' in row and 'number' in row['formula']:
            return row['formula']['number']
        return None