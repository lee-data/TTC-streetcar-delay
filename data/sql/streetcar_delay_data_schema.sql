-- delete table if it exists
DROP TABLE IF EXISTS Streetcar_Delay_Data;

CREATE TABLE Streetcar_Delay_Data (
    incident_date TEXT,
    line TEXT,
    incident_time TEXT,
    day_of_week TEXT,
    location TEXT,
    incident TEXT,
    min_delay INTEGER,
    min_gap INTEGER,
    bound TEXT,
    vehicle TEXT
);

