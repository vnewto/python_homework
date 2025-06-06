##TASK 1

#import logging module
import logging

#configure logging 
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO) #will print everything info level and above
logger.addHandler(logging.FileHandler("./decorator.log","a")) #write logs to a file in append mode

#declare decorator function
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        logger.log(logging.INFO, f"Function Name: {func.__name__}") #log function name
        #log arguments or kw arguments, if none then log "None"
        if args:
            logger.log(logging.INFO, f"Positional Parameters: {args}")
        elif kwargs:
            logger.log(logging.INFO, f"Positional Parameters: {kwargs}")
        else:
            logger.log(logging.INFO, "Positional Parameters: None")
        result = func(*args, **kwargs) #declare variable named result
        logger.log(logging.INFO, f"Returned Result: {result}") #log the result
        return result
    return wrapper

#declare function that takes no parameters and returns nothing. Use decorator
@logger_decorator
def empty_function():
    print("empty_function has been run.")

#Declare a function that takes a variable number of positional arguments and returns True. Use decorator
@logger_decorator
def returns_true(*args):
    if args:
        return True

#Declare function that takes no positional arguments and a variable number of keyword arguments, and that returns logger_decorator. Use decorator
@logger_decorator
def input_kwargs(**kwargs):
    if kwargs:
        return logger_decorator

#call all functions
empty_function()
returns_true(4, 5, 6)
input_kwargs(Location="Paris", Language="French", Continent="Europe")