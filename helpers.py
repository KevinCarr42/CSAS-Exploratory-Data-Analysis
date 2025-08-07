import pandas as pd
from sqlalchemy import create_engine


def sql(query, dialect='mysql', driver='mysqlconnector', username='root', password='root', host='localhost',
        port='3306', database='dmapps_0', disambiguate=True):
    engine = create_engine(f'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}')
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
        if disambiguate:
            counts = {}
            new_cols = []
            for col in df.columns:
                if col in counts:
                    counts[col] += 1
                    new_cols.append(f"{col}_{counts[col]}")
                else:
                    counts[col] = 0
                    new_cols.append(col)
            df.columns = new_cols
        return df
