import pandas as pd
import sqlite3

connection_db = sqlite3.connect("cyberchase.db")

# Checking the tables in the database
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table';", connection_db)
print(tables)

query_1 = "SELECT * FROM episodes"

data_sql = pd.read_sql(query_1, connection_db)
print(data_sql.head().to_string())

data_sql.to_csv("episodes.csv", index = False)