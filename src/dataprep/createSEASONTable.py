import sqlite3
from datetime import datetime, timedelta
import os

# Function to create Season table and insert dates
def create_season_table(db_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Drop Season table if it exists
    cursor.execute('DROP TABLE IF EXISTS Season')
    
    # Create Season table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Season (
            date TEXT PRIMARY KEY,
            season TEXT
        )
    ''')
    
    # Define the date range
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    delta = timedelta(days=1)
    
    # Define season ranges (approximate dates for Canada)
    def get_season(date):
        year = date.year
        if datetime(year, 3, 20) <= date < datetime(year, 6, 21):
            return f'Spring {year}'
        elif datetime(year, 6, 21) <= date < datetime(year, 9, 22):
            return f'Summer {year}'
        elif datetime(year, 9, 22) <= date < datetime(year, 12, 21):
            return f'Fall {year}'
        else:
            return f'Winter {year}'

    # Insert dates into Season table
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.strftime('%Y-%m-%d')
        season = get_season(current_date)
        
        # Insert data into the table
        cursor.execute('''
            INSERT INTO Season (date, season)
            VALUES (?, ?)
        ''', (date_str, season))
        
        current_date += delta
    
    conn.commit()
    conn.close()

# Get the directory two levels up from the current script
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Construct the relative path to the database
db_path = os.path.join(base_dir, 'data', 'streetcardelaydb.db')

# Call the function to create and populate the Season table
create_season_table(db_path)
print('Season table created and populated successfully')
