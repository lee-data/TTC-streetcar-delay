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

    # Load Line table to get lineType
    line_table_name = 'Line'  # Replace with your line table name
    line_df = load_from_db(db_name, line_table_name)

    # Ensure lineType is set to 4 if Streetcar_Delay_Data.line value is not found in Line.lineId
    line_df['lineType'] = line_df['lineType'].fillna(4) # Assuming 4 is the default value
    
    # Merge the dataframes on lineId
    df = df.merge(line_df[['lineId', 'lineType']], left_on='line', right_on='lineId', how='left')

    # Load Delay table to get delayType
    delay_table_name = 'Delay'  # Replace with your delay table name
    delay_df = load_from_db(db_name, delay_table_name)

    # Function to determine delayType
    def get_delay_type(min_delay):
        for _, row in delay_df.iterrows():
            if row['delayFrom'] <= min_delay <= row['delayTo']:
                return row['delayId']
        return None

    # Apply the function to determine delayType
    df['delayType'] = df['min_delay'].apply(get_delay_type)

    # Display the DataFrame
    #print(df)
    
    #for lineType that has not been set, set it to 4
    df['lineType'] = df['lineType'].fillna(4)
    
    #show 20 records where lineType is set to 4
    print(df[df['lineType']==4].head(20))
        
if __name__ == "__main__":
    main()
