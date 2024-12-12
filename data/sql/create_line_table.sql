
--drop Line table if exists;
DROP TABLE IF EXISTS Line;


--create Line table with lineId, lineType, lineName
CREATE TABLE Line (
    lineId TEXT,
    lineType TEXT,
    lineName TEXT
);

INSERT INTO Line (lineId, lineType, lineName) VALUES
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
('519', 'Limited', 'Unknown');


