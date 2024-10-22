import pandas as pd
import sqlite3

# Function to read data from an XLSX file
def read_xlsx(file_path):
    return pd.read_excel(file_path)

# Function to insert data into SQLite database
def insert_into_db(df, db_name, table_name):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()

# Main function
def main():
    xlsx_file_2023 = '01_src/data/ttc-streetcar-delay-data-2023.xlsx'  # Replace with your first XLSX file path
    xlsx_file_2024 = '01_src/data/ttc-streetcar-delay-data-2024.xlsx'  # Replace with your second XLSX file path
    db_name = '01_src/db/streetcardelaydb.db'  # Replace with your SQLite database name
    table_name = 'streetcar_delay_data'  # Replace with your table name

    # Read data from both XLSX files
    df_2023 = read_xlsx(xlsx_file_2023)
    df_2024 = read_xlsx(xlsx_file_2024)

    # Combine the data
    combined_df = pd.concat([df_2023, df_2024], ignore_index=True)

    # Insert combined data into SQLite database
    insert_into_db(combined_df, db_name, table_name)

if __name__ == "__main__":
    main()
    
