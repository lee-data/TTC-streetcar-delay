import pandas as pd
import sqlite3
import os

# Function to read data from an XLSX file
def read_xlsx(file_path):
    return pd.read_excel(file_path)

# Function to clear all records from a table in SQLite database
def clear_table(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table_name}")
    conn.commit()
    conn.close()

# Function to insert data into SQLite database
def insert_into_db(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    conn.close()

# Main function
def main():
    # Get the directory of the current script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

    # Construct relative paths
    xlsx_file_2023 = os.path.join(base_dir, 'data', 'raw', 'ttc-streetcar-delay-data-2023.xlsx')
    xlsx_file_2024 = os.path.join(base_dir, 'data', 'raw', 'ttc-streetcar-delay-data-2024.xlsx')
    db_name = os.path.join(base_dir, 'data', 'streetcardelaydb.db')
    table_name = 'Streetcar_Delay_Data'  # Replace with your table name

    # Read data from both XLSX files
    df_2023 = read_xlsx(xlsx_file_2023)
    df_2024 = read_xlsx(xlsx_file_2024)

    # Combine the data
    combined_df = pd.concat([df_2023, df_2024], ignore_index=True)

    # Clear the existing records from the table
    clear_table(db_name, table_name)
    
    # Insert combined data into SQLite database
    insert_into_db(combined_df, db_name, table_name)
    
    print("Data loaded successfully from xlsx to DB!")

if __name__ == "__main__":
    main()
