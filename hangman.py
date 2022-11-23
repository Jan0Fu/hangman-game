import random
import string


def random_words():
    words = ["astronaut", "electricity", "virus", "paranoid", "velociraptor", "princess", "therapeut"]
    word = random.choice(words)
    return word.upper()
    
def hangman():
    word = random_words()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set() 
    print(word)

    while len(word_letters) > 0:
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("You have already used that character, try something else")
        else:
            print("Invalid character, try again")

hangman()



