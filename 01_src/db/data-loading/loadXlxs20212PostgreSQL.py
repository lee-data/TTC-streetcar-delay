import pandas as pd
from sqlalchemy import create_engine, text

# Read excel file and insert data from all xlsx sheets into database
excel_file = '01_src/data/ttc-streetcar-delay-data-2021.xlsx'
sheets = pd.read_excel(excel_file, engine='openpyxl', sheet_name=None)

# Connect to PostgreSQL database
db_user = 'admin'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'
db_name = 'streetcardelaydb'

engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

table_name = 'streetcar_delay_data'

# Clear table before inserting new data
with engine.connect() as connection:
    connection.execute(text(f'TRUNCATE TABLE {table_name}'))
    print('Table cleared successfully')

# Iterate over each sheet and insert data into the database
for sheet_name, df in sheets.items():
    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f'Data from sheet {sheet_name} inserted successfully')

# Generate SQL file to recreate PostgreSQL schema
with open('01_src/db/streetcar_delay_data_schema.sql', 'w') as file:
    file.write(f'CREATE TABLE {table_name} (\n')
    for column in df.columns:
        file.write(f'    {column} VARCHAR,\n')
    file.write(');')
    
print('Schema file generated successfully')

# Query data from database and generate file to write query results into another database using 
# insert into statements
query = f'SELECT * FROM {table_name}'
df = pd.read_sql(query, engine)

with open('01_src/db/streetcar_delay_data_2021_insert.sql', 'w') as file:
    for index, row in df.iterrows():
        file.write(f"INSERT INTO {table_name} VALUES (")
        for value in row:
            file.write(f"'{value}', ")
        file.write(');\n')
        
print('Insert file generated successfully')
