

# This module establishes a connection to a Microsoft SQL Server database using SQLAlchemy.
# It saves the final processed DataFrame to the specified table, appending new records.


import urllib.parse
from sqlalchemy import create_engine
import urllib


def save_to_sql(df, table_name, server, database, username, password):

    conn_string = f'DRIVER = {{ODBC Driver 17 for SQL Server}};'\
                    f'SERVER ={server};'\
                    f'DATABASE = {database};'\
                    f'UID = {username};'\
                    f'PWD = {password};'
    
    conn_url = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(conn_string)

    engine = create_engine(conn_url)

    df.to_sql(table_name, con= engine, if_exists= 'append', index = False)