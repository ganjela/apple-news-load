from load import Loader
from utils.helpers import convert_to_utc
import pandas as pd
import json


def main(request):
    response = request.get_json()["transformed_data"]
    data: dict = json.loads(response)
    df = pd.DataFrame(data)
    convert_to_utc(df)

    Loader().load(df)

    return {"status": "success"}
