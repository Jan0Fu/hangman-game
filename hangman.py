import random
import string

words = ["astronaut", "electricity", "virus", "paranoid", "velociraptor", "princess", "therapeut"]

def hangman():
    word = random.choice(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    user_letter = input("Guess a letter: ").upper()




