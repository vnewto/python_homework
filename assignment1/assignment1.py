# Write your code here.

#Task 1
def hello():
    return "Hello!"
print(hello())

#Task 2
def greet(name):
    return f"Hello, {name}!"
print(greet("Name"))

#Task 3
def calc(num1, num2, operation = "multiply"):
    try:   
        match operation:
            case "add":
                return num1 + num2
            case "subtract":
                return num1 - num2
            case "multiply":
                return num1 * num2
            case "divide":
                return num1 / num2
            case "modulo":
                return num1 % num2
            case "int_divide":
                return num1 // num2
            case "power":
                return num1 ** num2

    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print("add: ", calc(2, 3, "add"))
print("subtract: ", calc(2, 3, "subtract"))
print("multiply: ", calc("2", 3, "multiply"))
print("divide: ", calc(2, 0, "divide"))
print("modulo: ", calc(2, 3, "modulo"))
print("int_divide: ", calc(2, 3, "int_divide"))
print("power: ", calc(2, 3, "power"))
print("invalid operation: ", calc(2, 3, "sqroot"))

#Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "str":
                return str(value)
            case "int":
                return int(value)
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
print("data_type_conversion: convert hello to int: ", data_type_conversion("hello", "int"))
print("data_type_conversion: convert 2 to int: ", data_type_conversion("2", "int"))

#Task 5
def grade(*args):
    try:    
        sum_args = sum(args)
        len_args = len(args)
        grade = sum_args / len_args
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        elif grade < 60:
            return "F"
    except Exception:
        return "Invalid data was provided."
    
print("grade(100, 50): ", grade(100, 50))
print("grade(90, 70, 80): ", grade(90, 70, 80))
print("grade('90', 70, 80): ", grade("90", 70, 80))

#Task 6
def repeat(string, count):
    #define empty string
    new_string = ""
    #iterate over string
    for x in string:
        #add letters to the new string
        new_string += x
    return new_string * count
print(repeat("hello", 4))

#Task 7
def student_scores(score_type, **kwargs):
    match score_type:
        case "mean":
            sum = 0
            for value in kwargs.values():
                sum += value
            return sum / len(kwargs)
        case "best":
            #get highest grade from the list
            best_grade = max(kwargs.values())
            print("best_grade: ", best_grade)
            #iterate over the kwargs and return the name associated with the high grade
            for key, value in kwargs.items():
                if value == best_grade:
                    return key
print("student_scores, best, Bob=100, Amy=90, Sally=80: ", student_scores("best", Bob=100, Amy=90, Sally=80))
print("student_scores, mean, Bob=100, Amy=90, Sally=80: ", student_scores("mean", Bob=100, Amy=90, Sally=80))

#Task 8
def titleize(string):
    #define a list of "little" words
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    #split string into list
    string_list = string.split()
    #capitalize the first and last word of string_list
    string_list[0] = string_list[0].capitalize()
    string_list[-1] = string_list[-1].capitalize()
    #iterate over list starting at position 1 and ending at the list length
    for i in range(1, len(string_list)-1):
        #if it's NOT a little word, capitalize it
        if string_list[i] not in little_words:
            string_list[i] = string_list[i].capitalize()
    #join list back together as a string
    return " ".join(string_list)

print("final title: ", titleize("harry potter and the sorcerer's stone"))
print("final title: ", titleize("harry potter and the chamber of secrets"))
print("final title: ", titleize("a on an the of and is in"))

#Task 9
def hangman(secret, guess):
    #turn secret into a list of characters
    secret_list = list(secret)
    #define a list of "_" characters the same length as the secret
    char_list = list(len(secret) * "_")
    #iterate through the secret letters
    for i in range(len(secret_list)):
        for x in guess:
            #check if the guess is present in the string
            #if a match, replace char_list with the correct letter at the correct index
            if x == secret_list[i]:
                char_list[i] = x
    #return joined string from char_list
    return "".join(char_list)
    
print("hangman correct guess: ", hangman("phone", "on"))
print("hangman correct guess: ", hangman("anonymous", "aou"))
print("hangman incorrect guess: ", hangman("phone", "kl"))


#Task 10
def pig_latin(string):
    #split string into a list
    word_list = string.split()
    #define a list of vowels
    vowels = ["a", "e", "i", "o", "u"]
    #define a list of consonants
    consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "r", "s", "t", "v", "w", "x", "y", "z"]
    #iterate over the word list
    for i in range(len(word_list)):
        #if string starts with a vowel, add "ay" to the end
        if word_list[i][0].lower() in vowels:
            word_list[i] = word_list[i] + "ay"
        else:
            #if string starts with "qu", move the "qu" to the end and add "ay"
            if len(word_list[i]) > 1 and word_list[i][0:2].lower() == "qu":
                word_list[i] = word_list[i][2:] + "quay"
            else:
                #find out what index # the first vowel is for each word
                first_vowel = 0
                for j in range(len(word_list[i])):
                    if word_list[i][j].lower() in vowels:
                        #return the value of j
                        first_vowel = j
                        print("word_list[i]: ", word_list[i])
                        print("first_vowel: ", first_vowel)
                        break
                #if vowel position > 0, create a consonant cluster from 0 to j
                if first_vowel > 0:
                    consonants = word_list[i][0:int(first_vowel)]
                    print("consonants: ", consonants)
                    #if consonant cluster ends with a q and the next letter is u, move consonant cluster + u to the end of the word and add "ay"
                    if consonants[-1] == "q" and word_list[i][first_vowel] == "u":
                        word_list[i] = word_list[i][first_vowel + 1:] + consonants + "uay"
                    else:    
                        #move consonant cluster to the end of the word and add "ay"
                        word_list[i] = word_list[i][first_vowel:] + consonants + "ay"
                        print("new word + ay: ", word_list[i])
    return " ".join(word_list)
                


print("pig_latin: ", pig_latin("coding is quite challenging"))
print("pig_latin: ", pig_latin("quick do another example"))
print("pig_latin: ", pig_latin("three blind mice"))
print("pig_latin: ", pig_latin("square"))