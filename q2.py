# %%
import pandas as pd
def get_employees_df():


  return pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/acbb2271e66c10a5b73aacf82"
        "ca82784/raw/e38afe62e088394d61ed30884dd50a6826eee0a8/employees.csv"
  )
def get_departments_df():
  dep_df = pd.read_csv(
      "https://gist.githubusercontent.com/kevin336/5ea0e96813aa88871c20d315b5"
        "bf445c/raw/d8fcf5c2630ba12dd8802a2cdd5480621b6a0ea6/departments.csv"
  )
  dep_df = dep_df.rename(columns={"DEPARTMENT_ID": "DEPARTMENT_IDENTIFIER"})


  return dep_df


employees = get_employees_df()
departments = get_departments_df()

#show dfs 
print(employees)
print(departments)


# 1. Please calculate the average, median, lower and upper quartiles of an employees' salaries.

average = employees["SALARY"].mean()
median = employees["SALARY"].median()
upper_quartile = employees["SALARY"].quantile(0.75)

print("Average salary: ", average)
print("Median salary: ", median)
print("Upper quartile: ", upper_quartile)
#2. Please calculate the average salary per department. Please include the department name in the results.
merged_df = pd.merge(employees, departments, left_on="DEPARTMENT_ID", right_on="DEPARTMENT_IDENTIFIER")
merged_df.head()

#Calculate average salary per department
avg_salary_dep = merged_df.groupby("DEPARTMENT_NAME")["SALARY"].mean()
print("Average salary per department")
print(avg_salary_dep)

# 3. Please create a new column named `SALARY_CATEGORY` with value "low" when the salary is lower than average and "high" if is it higher or equal.
#Calculate average salary
employees["SALARY_CATEGORY"] = employees["SALARY"].apply(lambda x: "low" if x < average else "high")
print(employees["SALARY_CATEGORY"])

# 4. Please create another column named `SALARY_CATEGORY_AMONG_DEPARTMENT` with value "low" when the employee salary is lower than average in his / her department and "high" in the other case.
avg_salary_dep = merged_df.groupby("DEPARTMENT_ID")["SALARY"].mean()
employees["SALARY_CATEGORY_AMONG_DEPARTMENT"] = employees.apply(lambda x: "low" if x["SALARY"] < avg_salary_dep[x["DEPARTMENT_ID"]] else "high", axis=1)

# 5. Please filter the dataframe `employees` to include only the rows where `DEPARTMENT_ID` equals to 20. Assign the result to new variable.
dep_20 = employees[employees["DEPARTMENT_ID"] == 20]
print(dep_20)

# 6. Please increase the salary by 10% for all employees working at the department 20.
dep_20["SALARY"] = dep_20["SALARY"] * 1.1


# 7. Please check if any of the `PHONE_NUMBER` column values are empty.
print(employees["PHONE_NUMBER"].isnull().values.any())
# there isnt

