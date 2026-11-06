import pandas as pd
df = pd.read_csv("Employee.csv")
print("========== EMPLOYEE DATA ANALYSIS ==========\n")
print("First 5 Employees:")
print(df.head())
print("\n\nDataset Information:")
print("Number of Employees:", len(df))
print("Number of Columns:", len(df.columns))

average_age = df["Age"].mean()
print("\nAverage Age of Employees:", round(average_age, 2))

average_experience = df["ExperienceInCurrentDomain"].mean()
print("Average Experience:", round(average_experience, 2), "years")

city_count = df["City"].value_counts()
print("\nEmployees by City:")
print(city_count)

education_count = df["Education"].value_counts()
print("\nEmployees by Education:")
print(education_count)

gender_count = df["Gender"].value_counts()
print("\nEmployees by Gender:")
print(gender_count)

age_limit = 30
employees_above_30 = df[df["Age"] > age_limit]
print("\nEmployees Above Age", age_limit, ":")
print(employees_above_30.head(10))
print("Total Employees Above 30:", len(employees_above_30))

experience_limit = 5
experienced_employees = df[
    df["ExperienceInCurrentDomain"] >= experience_limit
]
print("\nEmployees With 5 or More Years Experience:")
print(experienced_employees.head(10))
print("Total Experienced Employees:", len(experienced_employees))

employees_left = df[df["LeaveOrNot"] == 1]
print("\nEmployees Who Left the Company:")
print(employees_left.head(10))
print("Total Employees Who Left:", len(employees_left))

employees_staying = df[df["LeaveOrNot"] == 0]
print("\nEmployees Still Working:")
print("Total Employees Still Working:", len(employees_staying))

employees_above_30.to_csv(
    "employees_above_30.csv",
    index=False
)
print("\nFiltered employee data exported successfully!")
print("File created: employees_above_30.csv")

experienced_employees.to_csv(
    "experienced_employees.csv",
    index=False
)

print("File created: experienced_employees.csv")

print("\n========== PROJECT SUMMARY ==========")

print("Total Employees:", len(df))
print("Average Age:", round(average_age, 2))
print("Average Experience:",
      round(average_experience, 2), "years")

print("\nMost Common City:",
      df["City"].value_counts().idxmax())

print("Most Common Education:",
      df["Education"].value_counts().idxmax())

print("Employees Who Left:", len(employees_left))
print("Employees Still Working:", len(employees_staying))

print("\n========== PROJECT COMPLETED ==========")