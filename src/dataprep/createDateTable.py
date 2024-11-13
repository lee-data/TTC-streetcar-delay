import sqlite3
from datetime import datetime, timedelta
import os

# Function to create Date table and insert dates
def create_date_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Drop Date table if it exists
    cursor.execute('DROP TABLE IF EXISTS Date')
    
    # Create Date table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Date (
            date TEXT PRIMARY KEY,
            holidayType TEXT,
            isWeekend TEXT
        )
    ''')
    
    # Define the date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = timedelta(days=1)
    
    # Define holidays with their names
    holidays = {
        '2023-01-01': "New Year's Day",
        '2023-02-20': "Family Day",
        '2023-04-07': "Good Friday",
        '2023-05-22': "Victoria Day",
        '2023-07-01': "Canada Day",
        '2023-07-03': "Canada Day",  # Observed holiday since July 1 is a Saturday
        '2023-09-04': "Labour Day",
        '2023-10-09': "Thanksgiving",
        '2023-12-25': "Christmas Day",
        '2023-12-26': "Boxing Day",
        '2024-01-01': "New Year's Day",
        '2024-02-19': "Family Day",
        '2024-03-29': "Good Friday",
        '2024-05-20': "Victoria Day",
        '2024-07-01': "Canada Day",
        '2024-09-02': "Labour Day",
        '2024-10-14': "Thanksgiving",
        '2024-12-25': "Christmas Day",
        '2024-12-26': "Boxing Day"
    }
    
    # Insert dates into Date table
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        is_weekend = "yes" if current_date.weekday() >= 5 else "no"
        holidayType = holidays.get(date_str, None)  # None if not a holiday
                
        # Insert data into the table
        cursor.execute('''
            INSERT INTO Date (date, holidayType, isWeekend)
            VALUES (?, ?, ?)
        ''', (date_str, holidayType, is_weekend))
        
        current_date += delta
    
    conn.commit()
    conn.close()

# Get the directory two levels up from the current script
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Construct the relative path to the database
db_path = os.path.join(base_dir, 'data', 'streetcardelaydb.db')

# Call the function to create and populate the Date table
create_date_table(db_path)
print('Date table created and populated successfully')
