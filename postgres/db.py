import pandas as pd
from sqlalchemy import create_engine
import os
import sys

rpath = os.path.abspath('..')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from postgresql_connection import create_database_engine
from tables.agriculture_table import create_agriculture_table
from insert_data import map_dataframe_to_agriculture_table

def populate():
    engine = create_database_engine()
    create_agriculture_table(engine)

    file_path = './data/Crop and fertilizer dataset.csv'
    df = pd.read_csv(file_path)

    map_dataframe_to_agriculture_table(engine, df)

if __name__ == "__main__":
    populate()
