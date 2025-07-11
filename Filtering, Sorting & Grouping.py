import pandas as pd

# Create a Dataframe with sample data
data = pd.DataFrame({
    "Name":["Anna", "Karen", "John", "Alice", "Kevin", "Sanna", "Bob", "Emily"],
    "Age":[35, 30, 57, 65, 25, 19, 20, 65],
    "Salary":[20000, 60000, 145000, 170000, 30000, 10000, 220000, 120000],
    "Department":["Tech", "Tech", "Tech", "HealthCare", "Operations", "Operations", "Tech", "Tech"]
})

# Sorting
# Ascending: smallest value at the top and values keep increasing
print("\n", data.sort_values(by = "Salary", ascending = True))

# Descending: largest value at the top and values keep decreasing
print("\n", data.sort_values(by = "Salary", ascending = False))


# Grouping
print("\n", data.groupby("Department")["Name"].count())

# Average salary per department
print("\n", data.groupby("Department")["Salary"].mean())

# Minumum salary per department
print("\n", data.groupby("Department")["Salary"].min())

# Maximum salary per department
print("\n", data.groupby("Department")["Salary"].max())

# Minimum age per department
print("\n", data.groupby("Department").agg({"Age":"min"}))

# Maximum age per department
print("\n", data.groupby("Department").agg({"Age":"max"}))


# Filtering
print(data[data["Salary"] > 100000])
print("\n", data[(data["Salary"] > 100000) & (data["Salary"] < 200000)])
print("\n", data[data["Age"].isin([20, 65])])

# Loading the CSV file
data_csv = pd.read_csv("./Python-For-Data-Science-main/Data/percent_bachelors_degrees_women_usa.csv")
# print(data_csv.head(2))