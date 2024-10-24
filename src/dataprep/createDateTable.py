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
            isHoliday BOOLEAN,
            isWeekend BOOLEAN,
            isEndOfMth BOOLEAN
        )
    ''')
    
    # Define the date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = timedelta(days=1)
    
    # Insert dates into Date table
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        is_weekend = current_date.weekday() >= 5
        is_end_of_month = (current_date + delta).month != current_date.month
        
        holidays = {
            '2023-01-01', '2023-02-20', '2023-04-07', '2023-04-10', '2023-05-22', 
            '2023-07-01', '2023-08-07', '2023-09-04', '2023-10-09', '2023-12-25', 
            '2023-12-26', '2024-01-01', '2024-02-19', '2024-03-29', '2024-04-01', 
            '2024-05-20', '2024-07-01', '2024-08-05', '2024-09-02', '2024-10-14', 
            '2024-12-25', '2024-12-26'
        }
        is_holiday = date_str in holidays
        
        cursor.execute('''
            INSERT INTO Date (date, isHoliday, isWeekend, isEndOfMth)
            VALUES (?, ?, ?, ?)
        ''', (date_str, is_holiday, is_weekend, is_end_of_month))
        
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