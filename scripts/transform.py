import pandas as pd
from scripts.extract import extract

data = extract()


def transform_data():
    df = pd.DataFrame(data)
    df = df.dropna()
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)
    return df

