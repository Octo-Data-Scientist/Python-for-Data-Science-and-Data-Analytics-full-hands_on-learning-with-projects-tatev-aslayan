# Importing libraries
import pandas as pd
import sqlite3

# Loading CSV file with header
data_csv = pd.read_csv("./Python-For-Data-Science-main/Data/percent_bachelors_degrees_women_usa.csv", encoding = 'utf-8')
print(data_csv)
print("\n", data_csv.shape)
print("\n", data_csv.columns, "\n")

# Loading a TXT file with header and separator coma
data_txt = pd.read_csv("./Python-For-Data-Science-main/Data/StudentSchools.txt", header = 0, sep = ",")
print(data_txt.head())
print("\n", data_txt.shape)

# Loading Excel file with specifically spreadsheet with name "Sheet1"
data_excel = pd.read_csv("file_name.xlsx", sheet_name = "Sheet1")

# Loading JSON file
data_json = pd.read_json("file_name.json")

# Loading SQL Table with table name "table_name"
## making connection with SQL database named "database_name.db"
connection_db = sqlite3.connect("database_name.db")

## 1st query to select 1 feature with name col_1 from table with "table_name"
query_1 = "SELECT col_1 FROM table_name"

## 2nd query to select all features with from table with "table_name"
query_2 = "SELECT * FROM table_name"

## loading ba tale with query_2 from SQL database
data_sql = pd.read_sql(query_2, connection_db)