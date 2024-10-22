#load from SQLite DB to DataFrame
import sqlite3
import pandas as pd

# Function to load data from SQLite database
def load_from_db(db_name, table_name):
    conn = sqlite3.connect(db_name)
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Main function
def main():
    db_name = '01_src/db/streetcardelaydb.db'  # Replace with your SQLite database name
    table_name = 'streetcar_delay_data'  # Replace with your table name

    # Load data from SQLite database
    df = load_from_db(db_name, table_name)

    # Display the DataFrame
    print(df)
    
if __name__ == "__main__":
    main()
    
