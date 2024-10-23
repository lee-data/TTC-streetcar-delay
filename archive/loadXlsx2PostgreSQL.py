import pandas as pd
from sqlalchemy import create_engine, text

# Read excel files
excel_file_2024 = '01_src/data/ttc-streetcar-delay-data-2024.xlsx'
df_2024 = pd.read_excel(excel_file_2024, engine='openpyxl')

excel_file_2023 = '01_src/data/ttc-streetcar-delay-data-2023.xlsx'
df_2023 = pd.read_excel(excel_file_2023, engine='openpyxl')

# Combine dataframes
df = pd.concat([df_2024, df_2023], ignore_index=True)

# Connect to PostgreSQL database
db_user = 'admin'
db_password = 'admin'
db_host = 'localhost'
db_port = '5432'
db_name = 'streetcardelaydb'

engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

table_name = 'streetcar_delay_data'

# Delete all rows from table
with engine.connect() as connection:
    connection.execute(text(f'DELETE FROM {table_name}'))
    
print('Data deleted from database successfully')

# Insert data into table
df.to_sql(table_name, engine, if_exists='replace', index=False)

print('Data inserted to database successfully')

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

with open('01_src/db/streetcar_delay_data_insert.sql', 'w') as file:
    for index, row in df.iterrows():
        file.write(f"INSERT INTO {table_name} VALUES (")
        for value in row:
            file.write(f"'{value}', ")
        file.write(');\n')
        
print('Insert file generated successfully')
