from typing import Any, Dict, List
import pandas as pd

class DataTransform:
    def __init__(self, endpoint_list: List[Dict[str, Any]]) -> None:
        self.dataframe = pd.DataFrame(endpoint_list)

    def data_cards_transform(self) -> pd.DataFrame:
        df_cards = self.dataframe.copy()
        return df_cards

    def data_lists_tranform(self) -> pd.DataFrame:
        df_lists = self.dataframe.copy()
        return df_lists

    def data_members_tranform(self) -> pd.DataFrame:
        df_members = self.dataframe.copy()
        return df_members
