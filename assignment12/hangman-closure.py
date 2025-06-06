##TASK 4

import re

def make_hangman(secret_word): #write function that takes one argument
    guesses = [] #declare empty list
    #check length of secret_word
    secret_word_length = len(secret_word)
    #create a variable of underscores that's the same length as secret_word
    word_in_progress = ["_"] * secret_word_length

    def human_closure(letter): #declare function that takes one letter as a parameter
        #add the letter to the guesses array
        guesses.append(letter)
        #find the index numbers that match the guessed letter
        if letter in secret_word:
            indices = [match.start() for match in re.finditer(letter, secret_word)] #find index numbers of matching occurrences of the letter in the secret word
            #replace those underscores with the letter
            for i in range(len(indices)): 
                word_in_progress[int(indices[i])] = letter
        #print word_in_progress
        print(f"You have guessed the letters {guesses}. Your word is currently {' '.join(word_in_progress)}")
        #return true if word has been guessed, or false if not
        if ''.join(word_in_progress) == secret_word:
            return True
        else:
            return False

    return human_closure

#use input as secret word
secret_word = input("What is your secret word?").lower()

#make reference to function
hangman_game = make_hangman(secret_word)

#set game over condition to false
game_over = False

#make a loop so that the input keeps asking for a new letter as long as game_ongoing is true
while not game_over:
    guessed_letter = input("What letter would you like to guess?")
    if hangman_game(guessed_letter) == True:
        game_over = True
        print(f"You won! The word was {secret_word}. Great job!")


