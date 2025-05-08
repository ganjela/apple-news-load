import json
import os

import pandas as pd
from dotenv import load_dotenv
from google.cloud import bigquery

load_dotenv()


class Loader:
    def __init__(self):
        self.table_id = os.getenv("TABLE_ID")
        self.client = bigquery.Client()

    def load(self, data: str):
        data: dict = json.loads(data)
        df = pd.DataFrame(data)
        self.client.load_table_from_dataframe(df, self.table_id).result()
