import csv

def read_employees():
    employees = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r", newline="") as file:
            reader = csv.reader(file)
            first = True
            for row in reader:
                if first:
                    employees["fields"] = row
                    first=False
                else: 
                    rows.append(row)
            employees["rows"] = rows
        return employees
    except BaseException as e:
        print("An exception occurred: ", type(e).__name__)
        raise e

employees = read_employees()
print("employees: ", employees)

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column=column_index("employee_id")

def first_name(row_number):
    first_name_index = column_index("first_name")
    return employees["rows"][row_number][first_name_index]

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees["rows"]))

def employee_find_2(employee_id):
    return list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees["rows"]))

def sort_by_last_name():
    last_name_index = column_index("last_name")
    employees["rows"].sort(key = lambda row : row[last_name_index])
    return employees["rows"]

sort_by_last_name()
print("After sort: ", employees)

def employee_dict(row):
    return_dict = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            return_dict[field] = row[i]
    return return_dict

print("employee_dict: ", employee_dict(employees["rows"][2]))

def all_employees_dict():
    return_dict = {}
    for row in employees["rows"]:
        return_dict[row[employee_id_column]]=employee_dict(row)
    return return_dict

print("all_employees_dict: ", all_employees_dict())