# STEP 1A
import sqlite3
import pandas as pd

# STEP 1B
conn = sqlite3.connect("data.sqlite")


# STEP 2
df_first_five = pd.read_sql("""
SELECT employeeNumber, lastName
FROM employees
""", conn)
print("--- Step 2 ---")
print(df_first_five.head())

# STEP 3

df_five_reverse = pd.read_sql("""
SELECT lastName, employeeNumber
FROM employees
""", conn)
print("--- Step 3 ---")
print(df_five_reverse.head())

# STEP 4
df_alias = pd.read_sql("""
SELECT lastName, employeeNumber AS ID
FROM employees
""", conn)
print("--- Step 4 ---")
print(df_alias.head())

# STEP 5
df_executive = pd.read_sql("""
    SELECT *,
        CASE
            WHEN jobTitle = 'President'
              OR jobTitle = 'VP Sales'
              OR jobTitle = 'VP Marketing'
            THEN 'Executive'
            ELSE 'Not Executive'
        END AS role
    FROM employees
""", conn)
print("--- Step 5 ---")
print(df_executive.head())

# STEP 6
df_name_length = pd.read_sql("""
    SELECT LENGTH(lastName) AS name_length
    FROM employees
""", conn)
print("--- Step 6 ---")
print(df_name_length.head())

# STEP 7
df_short_title = pd.read_sql("""
    SELECT SUBSTR(jobTitle, 1, 2) AS short_title
    FROM employees
""", conn)
print("--- Step 7 ---")
print(df_short_title.head())

# STEP 8
sum_total_price = pd.read_sql("""
    SELECT SUM(ROUND(priceEach * quantityOrdered)) AS total_price
    FROM orderDetails
""", conn)["total_price"]
print("--- Step 8 ---")
print(sum_total_price)

# STEP 9
df_day_month_year =  pd.read_sql("""
    SELECT orderDate,
           STRFTIME('%d', orderDate) AS day,
           STRFTIME('%m', orderDate) AS month,
           STRFTIME('%Y', orderDate) AS year
    FROM orders
""", conn)
print("--- Step 9 ---")
print(df_day_month_year.head())

conn.close