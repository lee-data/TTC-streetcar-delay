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
    
    # Convert incident_date to datetime
    df['incident_date'] = pd.to_datetime(df['incident_date'])

    # Load Date table to get holidayType and isWeekend columns
    date_table_name = 'Date'  # Replace with your date table name
    date_df = load_from_db(db_name, date_table_name)
    date_df['date'] = pd.to_datetime(date_df['date'])

    # Merge Date table with Streetcar_Delay_Data table on incident_date
    df = df.merge(date_df[['date', 'holidayType', 'isWeekend']], left_on='incident_date', right_on='date', how='left')
    df.drop(columns=['date'], inplace=True)

    # Load Line table to get lineType
    line_table_name = 'Line'  # Replace with your line table name
    line_df = load_from_db(db_name, line_table_name)

    # Ensure lineType is set to 4 if Streetcar_Delay_Data.line value is not found in Line.lineId
    if 'lineId' in line_df.columns:
        line_df = line_df.set_index('lineId')
        df['lineType'] = df['line'].map(line_df['lineType']).fillna(4).astype(int)
    else:
        raise KeyError("Column 'lineId' not found in Line DataFrame")

    # Display the DataFrame
    print(df)

if __name__ == "__main__":
    main()
