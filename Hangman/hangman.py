import random
import string

from words import word


def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list 

    while '-' in word or ' ' in word:
        word = random.choice(words)
        

    return word

def hangman():
    word =  get_valid_word(word)
    word_letter = set(word) # letter in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #getting user input
    while len(word_letter) > 0:

        # letter userd
        print('You have used these characters: ',' '.join(used_letters))

        # what current word is 
        word_list = 

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that character. Please try again. ")

        else:
            print("Invalid Character. Please try again.")  

user_input = input('Type something: ')
