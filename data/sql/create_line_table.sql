
--drop Line table if exists;
DROP TABLE IF EXISTS Line;


--create Line table with lineId, lineType, lineName
CREATE TABLE Line (
    lineId TEXT,
    lineType INTEGER,
    lineName TEXT
);

INSERT INTO Line (lineId, lineType, lineName) VALUES
('301', 1, 'Queen'),
('304', 1, 'King'),
('305', 1, 'Dundas'),
('306', 1, 'Carlton'),
('310', 1, 'Spadina'),
('501', 2, 'Queen'),
('503', 2, 'Kingston Rd'),
('504', 2, 'King'),
('505', 2, 'Dundas'),
('506', 2, 'Carlton'),
('507', 3, 'Long Branch'),
('508', 3, 'Lake Shore'),
('509', 2, 'Harbourfront'),
('510', 2, 'Spadina'),
('511', 2, 'Bathurst'),
('512', 2, 'St. Clair');

