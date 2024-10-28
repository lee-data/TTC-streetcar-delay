
--drop Line table if exists;
DROP TABLE IF EXISTS Delay;

--create Line table with lineId, lineType, lineName
CREATE TABLE Delay (
    delayId INTEGER,
    delayFrom INTEGER,
    delayTo INTEGER,
    label TEXT
);

INSERT INTO Delay (delayId, delayFrom, delayTo, label) VALUES
(1, 0, 5, '0-5'),
(2, 6, 15, '6-15'),
(3, 15, 1000, '>16');

