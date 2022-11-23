import random
import string

words = ["astronaut", "electricity", "virus", "paranoid", "velociraptor", "princess", "therapeut"]

def hangman():
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    user_letter = input("Guess a letter: ").upper()

    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:
        print("You have already used that character, try something else")
    else:
        print("Invalid character, try again")



