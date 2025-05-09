import pandas as pd

def convert_to_utc(df):
    df['published_at'] = pd.to_datetime(df['published_at'],unit='ms',utc=True)
