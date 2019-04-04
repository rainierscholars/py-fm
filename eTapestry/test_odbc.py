# Tests ODBC connection to FileMaker

import pandas as pd
import pypyodbc as obdc

# Replace empty strings below with valid strings before running
dsn=''
database=''
table=''
user=''

con_str=f'DSN={dsn};Database={database};UID={user}'

db = obdc.connect(con_str)

sql = f'SELECT * FROM {table}'

df = pd.read_sql(sql=sql, con=db)

# Print rows in FileMaker table
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df)



