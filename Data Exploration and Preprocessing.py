import pandas as pd

# Loading CSV file 
df = pd.read_csv("./Python-For-Data-Science-main/Data/percent_bachelors_degrees_women_usa.csv")
print(df, "\n")

print(df.head(), "\n")
print(df.tail(), "\n")
print(f"Shape of the Dataframe: {df.shape}", "\n")
print(df.info(), "\n")
print(df.describe(), "\n")

# Checking for null values
print(df.isna().sum().any(), "\n")
# print(df.dropna())
# print(df.fillna("NULL"))

# Checking for duplicates
print(f"Are they duplicates in the dataframe? {df.duplicated().sum().any()}\n")

df = df.drop_duplicates()
df.reset_index(inplace = True)
print(df)

print(df.iloc[10], "\n")

data = pd.DataFrame({
    "A1":[1, 2, 3],
    "A2":[4, 5, 6],
    "A3":[7, 8, 9]
}, index = ["X", "Y", "Z"])
print(data, "\n")
print(data.loc["X"], "\n")
print(data.loc[:,"A2"], "\n")
print(data.loc["Y","A2"])