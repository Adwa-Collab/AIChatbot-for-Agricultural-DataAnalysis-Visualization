import os
import sys

rpath = os.path.abspath('../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import pandas as pd
from sqlalchemy import create_engine
from postgresql_connection import create_database_engine
from tables.agriculture_table import create_agriculture_table


def map_dataframe_to_agriculture_table(engine, dataframe):
    table_name = 'agriculture_table'
    dataframe.to_sql(table_name, engine, index=False, if_exists='replace')
