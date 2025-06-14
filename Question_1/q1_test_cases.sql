CREATE TABLE prices (
    date DATE, 
    ticker TEXT,
    volume INTEGER,
    price INTEGER
);

INSERT INTO prices (date, tickcer, volume, price) VALUES
('2020-01-01', 'MSFT', 232592, 323),
('2020-01-01', 'IBM', 293455, 134),
('2020-01-01', 'AAPL', 123456, 188),
('2020-01-02', 'AAPL', 123456, 188),
('2020-01-02', 'NFLX', 100000, 223);

CREATE TABLE names (
    ticker TEXT,
    name TEXT
);  

INSERT INTO names (ticker, name) VALUES
('MSFT', 'Microsoft Corp'),
('IBM', 'International Business Machines'),
('AAPL', 'Apple Inc'),
('NFLX', 'Netflix');