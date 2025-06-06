##TASK 2

def type_converter(type_of_output): #declare decorator that takes one argument
    def type_decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)
        return wrapper
    return type_decorator

#function that takes no arguments and returns the integer 5
@type_converter(str)
def return_int():
    return int(5)

#function that takes no arguments and returns a string
@type_converter(int)
def return_string():
    return "not a number"

y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen