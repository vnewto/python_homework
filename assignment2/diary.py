try:
    #open a file named diary.txt with append command
    with open("diary.txt", "a") as file:
        #Prompt for imput by asking "What happened today?"
        greeting = input("What happened today?")
        #add this line to the diary
        file.write(greeting + "\n")
        #indefinitely prompt for input "what else?"
        while True:
            what_else = input("What else?")
            #if "done for now" entered into input, close file
            if what_else.lower() == "done for now":
                break
            else:
                file.write(what_else + "\n")
except Exception as e:
    print(e)