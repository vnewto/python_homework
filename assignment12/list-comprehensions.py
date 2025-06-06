##TASK 3

import pandas as pd

#create dataframe from csv file
employees = pd.read_csv("../csv/employees.csv")
print(employees.head())

#declare empty list
employees_list = []

for row in employees.iterrows(): #iterate over rows
    employees_list.append(row[1]['first_name'] + " " + row[1]['last_name']) #add first name + last name to list

print("employees_list: ", employees_list)

#make list of employees with "e" in their name
employees_with_e = [x for x in employees_list if "e" in x]
print("employees_with_e: ", employees_with_e)