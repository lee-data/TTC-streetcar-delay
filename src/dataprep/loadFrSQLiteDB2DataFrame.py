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
    
    # Convert Incident_Date to datetime
    df['incident_date'] = pd.to_datetime(df['incident_date'])

    # Add isHoliday column (assuming you have a function or list of holidays)
    holidays = ['2023-01-01', '2023-12-25']  # Example holidays
    df['isHoliday'] = df['incident_date'].dt.strftime('%Y-%m-%d').isin(holidays)

    # Add isWeekend column
    df['isWeekend'] = df['incident_date'].dt.weekday >= 5

    # Add isEndOfMth column
    df['isEndOfMth'] = df['incident_date'].dt.is_month_end


    # Display the DataFrame
    print(df)
    
if __name__ == "__main__":
    main()
