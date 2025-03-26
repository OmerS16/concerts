import os
import pandas as pd
from sqlalchemy import create_engine

def upload_to_rds(df: pd.DataFrame, table_name: str = 'events'):
    """
    Uploads a Pandas DataFrame to an AWS RDS database table using SQLAlchemy.
    
    Assumes that the following environment variables are set:
      - RDS_USERNAME
      - RDS_PASSWORD
      - RDS_HOST
      - RDS_PORT (optional; defaults to 5432 for PostgreSQL)
      - RDS_DB_NAME

    :param df: Pandas DataFrame to upload.
    :param table_name: The target table name in the database.
    """

    username = os.environ.get('RDS_USERNAME')
    password = os.environ.get('RDS_PASSWORD')
    host = os.environ.get('RDS_HOST')
    port = os.environ.get('RDS_PORT', 5432)
    db_name = os.environ.get('RDS_DB_NAME')

    if not all([username, password, host, db_name]):
        raise Exception("One or more required RDS environment variables are missing.")

    connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}"
    
    engine = create_engine(connection_string)
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    print(f"Uploaded {len(df)} records to table '{table_name}' in database '{db_name}'.")
