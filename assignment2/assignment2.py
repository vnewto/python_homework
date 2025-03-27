#Task 2
import csv

def read_employees():
    #declare empty dictionary and empty list
    new_dict = {}
    rows_list = []
    #read csv file
    try:
        with open("../csv/employees.csv") as file:
            reader = csv.reader(file)
            #store row 1 in the dictionary using the key "fields"
            new_dict["fields"] = next(reader)
            #loop through the rows
            for row in reader:
                #store other rows in the rows list
                rows_list.append(row)
    except Exception as e:
        print(e)
    #add rows_list to dictionary using key "rows"
    new_dict["rows"] = rows_list
    #return new_dict
    return new_dict

employees = read_employees()
print("employees: ", employees)


#Task 3
def column_index(string):
    index_num = employees["fields"].index(string)
    return index_num
print("column_index: first_name: ", column_index("first_name"))
employee_id_column = column_index("employee_id")
print("employee_id_column: ", employee_id_column)


#Task 4
def first_name(row_num):
    #call column_index function using "first_name", assign it to a variable
    column_index_num = column_index("first_name")
    #search employees dictionary to retrieve the list at the row number
    list_items = employees.get("rows")[row_num]
    #get the value of the key "row" at index number column_index_num
    name = list_items[column_index_num]
    return name

print("first_name(1): ", first_name(1))
print("first_name(2): ", first_name(2))


#Task 5
def employee_find(employee_id):
    #input a row number
    def employee_match(row):
        #return the employee id number associated with that row number
        return int(row[employee_id_column]) == employee_id
    #go through the list of employees and make a list of the id #s
    matches=list(filter(employee_match, employees["rows"]))
    return matches

print("matches: ", employee_find(1))
print("matches: ", employee_find(12))


#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches


#Task 7
def sort_by_last_name():
    employees["rows"].sort(key=lambda row: row[column_index("last_name")])
    return employees["rows"]

print("sort_by_last_name: ", sort_by_last_name())


#Task 8
def employee_dict(row):
    #find index number of employee_id
    employee_id_index = int(column_index("employee_id"))
    #declare empty list
    employee_fields = []
    #turn employee_fields into a list
    for field in employees["fields"]:
        employee_fields.append(field)
    #convert employee_fields and row into tuples, excluding employee_id
    fields_tuple = tuple(employee_fields[employee_id_index + 1:])
    row_tuple = tuple(row[employee_id_index + 1:])
    #combine fields and row
    employee_info = dict(zip(fields_tuple, row_tuple))
    #turn "fields" into the keys for the dictionary
    
    #remove employee_id from the dict
    #return employee dictionary without employee id
    return employee_info

print("employee_dict: ", employee_dict(['6', 'Tracy', 'Foster', '+237 6225761379']))
print("employee_dict: ", employee_dict(['4', 'Kenneth', 'White', '+64 4924992211']))


#Task 9
def all_employees_dict():
    #declare empty dictionary
    dict_of_all_employees = {}
    #loop through employee rows with employee_dict function
    for row in employees["rows"]:
        #add employee id as key and row (without employee id) as value
        dict_of_all_employees.update({row[0]: employee_dict(row)})
    return dict_of_all_employees

print("all_employees_dict: ", all_employees_dict())


#Task 10
import os
def get_this_value():
    this_value = os.getenv('THISVALUE')
    return this_value

print("get_this_value: ", get_this_value())


#Task 11
import custom_module
def set_that_secret(a_new_secret):
    custom_module.set_secret(a_new_secret)

set_that_secret("a new secret password")
print(custom_module.secret)


#Task 12
#create a function to read a file and convert each row to a tuple
def read_file(file_name):
    try:
        with open(file_name) as file:
            reader = csv.reader(file)
            #create an empty dictionary and an empty rows list
            new_dict = {}
            rows_list = []
            #first row gets converted to "fields" in the dictionary
            new_dict["fields"] = next(reader)
            #loop through the file rows and add them to the rows_list
            for row in reader:
                rows_list.append(tuple(row))
    except Exception as e:
        print(e)
    #add rows_list to dictionary using key "rows"
    new_dict["rows"] = rows_list
    #return new_dict
    return new_dict

print("read_file minutes1: ", read_file("../csv/minutes1.csv"))
print("read_file minutes2: ", read_file("../csv/minutes2.csv"))

#perform read_file function on both files minutes1 and minutes2
def read_minutes():
    minutes1_dict = read_file("../csv/minutes1.csv")
    minutes2_dict = read_file("../csv/minutes2.csv")
    return minutes1_dict, minutes2_dict

minutes1, minutes2 = read_minutes()
print("minutes1: ", minutes1)
print("minutes2: ", minutes2)


#Task 13
def create_minutes_set():
    new_set_1 = set(minutes1["rows"])
    print("new_set_1: ", new_set_1)
    new_set_2 = set(minutes2["rows"])
    print("new_set_2: ", new_set_2)
    merged_set = new_set_1.union(new_set_2)
    return merged_set

print("create_minutes_set: ", create_minutes_set())
minutes_set = create_minutes_set()
print("minutes_set: ", minutes_set)


#Task 14
from datetime import datetime
def create_minutes_list():
    #create a list from the minutes_set
    minutes_list = list(minutes_set)
    new_minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return new_minutes_list

print("create_minutes_list: ", create_minutes_list())
minutes_list = create_minutes_list()
print("minutes_list: ", minutes_list)


#Task 15
def write_sorted_list():
    #sort minutes_list in ascending order of datetime
    minutes_list.sort(key=lambda x : x[1])
    #convert minutes list back to strftime using map method
    converted_minutes_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    #open minutes.csv file
    with open("./minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        for row in converted_minutes_list:
            writer.writerow(row)
    return converted_minutes_list

print("write_sorted_list(): ", write_sorted_list())
