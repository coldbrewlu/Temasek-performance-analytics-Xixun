-- input: price table & name table
-- join tables
-- computed field
-- window function
-- filtering top 3 rows per day
-- output data, rank, name, turnover


-- turnover computation CTE
WITH calculated_turnover AS(
    SELECT 
        p.date,
        n.name,
        SUM(p.volume * p.price) AS turnover -- in case duplocated (date, ticker) present in table
    FROM 
        prices p
    JOIN 
        names n ON p.ticker = n.ticker -- join with names table using ticker as a key
    GROUP BY 
        p.date, p.ticker, n.name
),

-- ranking CTE
ranked_turnover AS (
    SELECT
        date,
        name,
        turnover,
        ROW_NUMBER() OVER (PARTITION BY date ORDER BY turnover DESC) AS rank
    FROM
        calculated_turnover
)

-- keep only top 3 companies per date
SELECT
    date,
    rank,
    name,
    turnover
FROM
    ranked_turnover
WHERE
    rank <= 3                      -- only top 3 per day
ORDER BY
    date,                          -- sort by date first
    rank;                          -- then by rank within that date