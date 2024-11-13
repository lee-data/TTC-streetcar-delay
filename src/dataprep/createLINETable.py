import sqlite3
import os

# Function to create Line table and insert data
def create_line_table(db_name):
    # Connect to SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Drop Line table if it exists
    cursor.execute('DROP TABLE IF EXISTS Line')
    
    # Create Line table with lineId, lineType, and lineName columns
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Line (
            lineId TEXT PRIMARY KEY,
            lineType TEXT,
            lineName TEXT
        )
    ''')
    
    # Data to insert into Line table
    line_data = [
        ('301', 'Blue Night', 'Queen'),
        ('304', 'Blue Night', 'King'),
        ('305', 'Blue Night', 'Dundas'),
        ('306', 'Blue Night', 'Carlton'),
        ('310', 'Blue Night', 'Spadina'),
        ('300', 'Blue Night', 'Unknown'),
        ('500', 'Regular', 'Unknown'),
        ('501', 'Regular', 'Queen'),
        ('503', 'Regular', 'Kingston Rd'),
        ('504', 'Regular', 'King'),
        ('505', 'Regular', 'Dundas'),
        ('506', 'Regular', 'Carlton'),
        ('507', 'Limited', 'Long Branch'),
        ('508', 'Limited', 'Lake Shore'),
        ('509', 'Regular', 'Harbourfront'),
        ('510', 'Regular', 'Spadina'),
        ('511', 'Regular', 'Bathurst'),
        ('512', 'Regular', 'St. Clair'),
        ('519', 'Limited', 'Unknown')
    ]
    
    # Insert data into Line table
    cursor.executemany('INSERT INTO Line (lineId, lineType, lineName) VALUES (?, ?, ?)', line_data)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print('Line table created and populated successfully')

# Get the directory two levels up from the current script
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Construct the relative path to the database
db_path = os.path.join(base_dir, 'data', 'streetcardelaydb.db')

# Call the function to create and populate the Line table
create_line_table(db_path)
