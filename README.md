# temasek-performance-analytics-Xixun

# Question 1 - Top 3 Turnover by Day (PostgreSQL)
This script computes the **top 3 companies per day** based on **turnover**, defined as:
$$turnover = price \times volume$$

## Instructions for running the script
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
| date       | rank | name                            | turnover   |
|------------|------|----------------------------------|------------|
| 2020-01-01 | 1    | Microsoft Corp                   | 75127216   |
| 2020-01-01 | 2    | International Business Machines  | 39322970   |
| 2020-01-01 | 3    | Apple Inc                        | 23209728   |
| 2020-01-02 | 1    | Microsoft Corp                   | 23209728   |
| 2020-01-02 | 2    | Apple Inc                        | 23209728   |
| 2020-01-02 | 3    | Netflix                          | 22300000   |

(6 rows)

# Question 2 – Moving Average Calculator (Python)
This script calculates the M-day moving average of a time series of stock prices using an efficient sliding window algorithm.

## Instructions for running the script
In terminal, run ``` python Question_2/q2_test_cases.py  ``` in the project root directory.

You are expected to see ```All test cases passed!```

Test cases covered include:
* Regular moving average with multiple windows
* Edge case with window size 1 and equal to list length
* Invalid cases (e.g., M = 0, M > N)
* Floating-point output accuracy

# Question 3 - Performance Analytics
This repository contains a Python-based analysis of a portfolio manager’s investments in AAPL and TSLA from 2011 to 2020. The analysis includes calculating IRR, TWR, and TVPI, as well as generating daily portfolio positions and concluding insights about investment performance.

## Features Implemented

### Part (a) – Performance Metrics

- **IRR (Internal Rate of Return)** using custom Newton-Raphson implementation with date adjustment (XIRR style)
- **TWR (Time-Weighted Return)** neutralizing the impact of cash injections/withdrawals
- **TVPI (Total Value to Paid-In)** calculated using total invested, divested, and residual holdings

### Part (b) – Daily Portfolio Tracking

- Tracks **daily shares held**, **cashflows**, and **market value**
- Generates a timeline of **portfolio evolution** and transaction impact

### Part (c) – Performance Conclusion

- Compares performance of AAPL vs TSLA
- Assesses manager's market timing and stock selection
- Calculates portfolio-level allocation and return summary

## How to run the script
### 1. Install Python dependencies
```bash
pip install pandas numpy openpyxl
```
Run all cells in the Jupyeter notebook. Check the output at the end of each task. View as a scrollable element or open in a text editor for the full result.

## Expected Output


## Author
Lu Xixun
Temasek Performance Analytics
June 2025
