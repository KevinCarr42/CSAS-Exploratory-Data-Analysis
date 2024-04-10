import pandas as pd
from sqlalchemy import create_engine


def sql(query, dialect='mysql', driver='mysqlconnector', username='root', password='root', host='localhost',
        port='3306', database='dmapps'):
    engine = create_engine(f'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}')
    with engine.connect() as conn:
        return pd.read_sql(query, conn)
