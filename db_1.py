import pandas as pd
import sqlite3

connection_db = sqlite3.connect("longlist.db")

# Checking the tables in the database
tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type = 'table';", connection_db)
# print(tables)

# Loading the Authors Table
query_1 = "SELECT * FROM authors"

df_1 = pd.read_sql(query_1, connection_db)
print(df_1.head(), "\n")

# Loading the Authored Table
query_2 = "SELECT * FROM authored"

df_2 = pd.read_sql(query_2, connection_db)
print(df_2.head(), "\n")

# Loading the Books Table
query_3 = "SELECT * FROM books"

df_3 = pd.read_sql(query_3, connection_db)
print(df_3.head(), "\n")

# Loading the Publishers Table
query_4 = "SELECT * FROM publishers"

df_4 = pd.read_sql(query_4, connection_db)
print(df_1.head(), "\n")

# Loading the Ratings Table
query_5 = "SELECT * FROM ratings"

df_5 = pd.read_sql(query_5, connection_db)
print(df_5.head())

# Loading the Translators Table
query_6 = "SELECT * FROM translators"

df_6 = pd.read_sql(query_6, connection_db)
print(df_6.head(), "\n")

# Loading the Translated Table
query_7 = "SELECT * FROM translated"

df_7 = pd.read_sql(query_7, connection_db)
print(df_7.head())