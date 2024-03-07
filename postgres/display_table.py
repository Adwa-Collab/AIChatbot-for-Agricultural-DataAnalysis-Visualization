import pandas as pd
from sqlalchemy import create_engine, text
import os
import sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from postgresql_connection import create_database_engine

engine = create_database_engine()

table_name = input("Enter the table Name:")
query = text(f'SELECT * FROM "{table_name}"')

with engine.connect() as connection:
    result = connection.execute(query)
    df = pd.DataFrame(result.fetchall(), columns=result.keys())

print(df)
