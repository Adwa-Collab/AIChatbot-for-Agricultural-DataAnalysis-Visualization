import os, sys

rpath = os.path.abspath('../../')
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from sqlalchemy import create_engine, Column, Integer, String, Float, MetaData, Table
from postgres.postgresql_connection import create_database_engine

def create_agriculture_table(engine):
    metadata = MetaData()

    agriculture_table = Table(
        'agriculture_data',
        metadata,
        Column('district_name', String),
        Column('soil_color', String),
        Column('nitrogen', Float),
        Column('potassium', Float),
        Column('phosphorus', Float),
        Column('ph', Float),
        Column('rainfall', Float),
        Column('temperature', Float),
        Column('crop', String),
        Column('fertilizer', String),
        Column('link', String)
    )

    metadata.create_all(engine)
    print('Agriculture data table created successfully.')
    return agriculture_table