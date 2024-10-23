import sqlite3
import pandas as pd
from datetime import datetime
import os

#delete all records where min_delay = 0
def delete_zero_min_delay_records():
    # Get the directory two levels up from the current script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    # Construct the relative path to the database
    db_path = os.path.join(base_dir, 'data', 'streetcardelaydb.db')
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Delete records where min_delay = 0
    cursor.execute("DELETE FROM Streetcar_Delay_Data WHERE min_delay = 0")
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def modify_incident_date_format():
    # Get the directory two levels up from the current script
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    # Construct the relative path to the database
    db_path = os.path.join(base_dir, 'data', 'streetcardelaydb.db')
    
    # Connect to the database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Example modification: Update the date format in the database
    cursor.execute("UPDATE Streetcar_Delay_Data SET incident_date = strftime('%Y-%m-%d', incident_date)")
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

delete_zero_min_delay_records()
print('Zero min_delay records deleted successfully')

modify_incident_date_format()
print('Incident_Date format modified successfully')