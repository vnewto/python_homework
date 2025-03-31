import pandas as pd
import numpy as np

#Task 1
my_dict = {"Name": ['Alice', 'Bob', 'Charlie'], "Age": [25, 30, 35], "City": ['New York', 'Los Angeles', 'Chicago']}
#convert to data frame using pandas
task1_data_frame = pd.DataFrame(my_dict)
print("task_1_data_frame: ", task1_data_frame)
#make copy of data frame
task1_with_salary = task1_data_frame.copy()
#add salary column
task1_with_salary["Salary"] = [70000, 80000, 90000]
print("task1_with_salary: ", task1_with_salary)
#make copy of new data frame
task1_older = task1_with_salary.copy()
#increase all ages by 1
task1_older["Age"] = task1_older["Age"] + 1
print("task1_older with modified age: ", task1_older)
#save to csv without index nums
task1_older.to_csv("employees.csv", index=False)


#Task 2
#read employees csv file
task2_employees = pd.read_csv("employees.csv")
print("task2_employees: ", task2_employees)
#load json file into a data frame
json_employees = pd.read_json("additional_employees.json")
print("json_employees: ", json_employees)
#combine both the employees data frames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("more_employees: ", more_employees)


#Task 3
#assign a variable to the first three rows
first_three = more_employees.head(3)
print("first_three: ", first_three)
#assign a variable to the last two rows
last_two = more_employees.tail(2)
print("last_two: ", last_two)
#assign a variable to the shape
employee_shape = more_employees.shape
print("employee_shape: ", employee_shape)
#print info about the data frame
print("more_employees.info: ") 
more_employees.info()


#Task 4
#read dirty_data csv file and assign to data frame
dirty_data = pd.read_csv("dirty_data.csv")
print("dirty_data: \n", dirty_data)
#create a copy of dirty_data
clean_data = dirty_data.copy()
#remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("clean_data: \n", clean_data)
#convert age to numeric & handle missing values
clean_data["Age"] = pd.to_numeric(clean_data["Age"], errors="coerce")
print("clean_data[age changed to numeric]: \n", clean_data)
#convert salary to numeric & handle missing values
clean_data["Salary"] = pd.to_numeric(clean_data["Salary"], errors="coerce")
print("clean_data[salary changed to numeric]: \n", clean_data)
#fill in missing age values with mean
mean_age = clean_data["Age"].mean()
print("mean_age: ", mean_age)
clean_data["Age"] = clean_data["Age"].fillna(mean_age)
#fill in missing salary values with median
median_salary = clean_data["Salary"].median()
print("median_salary: ", median_salary)
clean_data["Salary"] = clean_data["Salary"].fillna(median_salary)
print("clean_data[salary and age filled in]: \n", clean_data)
#convert hire date to datetime
clean_data["Hire Date"] = pd.to_datetime(clean_data["Hire Date"], errors="coerce", format="mixed")
print("clean_data[hire date converted to datetime]: \n", clean_data)
#standardize name and dept to upper case
clean_data["Name"] = clean_data["Name"].str.upper()
print("clean_data[Name converted to uppercase]: \n", clean_data)
clean_data["Department"] = clean_data["Department"].str.upper()
print("clean_data[Department converted to uppercase]: \n", clean_data)