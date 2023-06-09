import pandas as pd
from scripts.extract import extract

data = extract()


def transform_data():
    df = pd.DataFrame(data)
    df = df.head(10)
    df.columns = ['column1', 'columns2']
    return df
