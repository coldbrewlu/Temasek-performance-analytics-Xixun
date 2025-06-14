# temasek-performance-analytics-Xixun

# Question 1 - Top 3 Turnover by Day (PostgreSQL)
This script computes the **top 3 companies per day** based on **turnover**, defined as:
$$turnover = price \times volume$$

## Instructions in running the script
### 1. Enter the PostgreSQL shall:
```bash
psql -U your_username -d temasek_test
```
Replace your_username with your PostgreSQL username.
Replace temasek_test with your test database name.

### 2. Load the test tables and data:
Inside psql, run:
```sql
\i Question_1/q1_test_cases.sql
```

### 3. Run the SQL Query:
```sql
\i Question_1/turnover_query.sql
```
You should be able to see expected output:
    date    | rank |              name               | turnover 
------------+------+---------------------------------+----------
 2020-01-01 |    1 | Microsoft Corp                  | 75127216
 2020-01-01 |    2 | International Business Machines | 39322970
 2020-01-01 |    3 | Apple Inc                       | 23209728
 2020-01-02 |    1 | Microsoft Corp                  | 23209728
 2020-01-02 |    2 | Apple Inc                       | 23209728
 2020-01-02 |    3 | Netflix                         | 22300000
(6 rows)


## Author
Lu Xixun
Temasek Performance Analytics
June 2025
