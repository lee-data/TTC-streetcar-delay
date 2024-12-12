# Load from SQLite DB to DataFrame
import sqlite3
import pandas as pd
import os

# Function to load data from SQLite database
def load_from_db(db_name, table_name):
    conn = sqlite3.connect(db_name)
    query = f'SELECT * FROM {table_name}'
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Main function
def main():
    # Get the directory two levels up from the current script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    # Construct the relative path to the database
    db_name = os.path.join(base_dir, 'data', 'streetcardelaydb.db')
    table_name = 'Streetcar_Delay_Data'  # Replace with your table name

    # Load data from SQLite database
    df = load_from_db(db_name, table_name)

    # Display the DataFrame
    print(df)
    
if __name__ == "__main__":
    main()
