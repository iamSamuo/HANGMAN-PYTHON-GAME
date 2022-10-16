


import random
import string

words = ["name", "come", "elevate","master","","calculate","elevetor","morning","endevours","movement","walk","explain","come","education",
"collabo ration","imagination","dwell","kill","ill"]

def get_valid_word(words):
    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)
    print(word)
    return word

    
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabets = set(string.ascii_uppercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:

        # .join(["a","b","c"]) ----> "abcd"
        print('You have', lives, 'You have used letters: ', ' '.join(used_letters))
        #what the current word is 

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()

        if user_letter in (alphabets - used_letters):
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1

        elif user_letter in used_letters:
            print("You have already guessed that letter")
        else:
            print("Invalid character. Please try again.")

    if lives == 0:
        print("You died!")
    else:
        print("Yeey! you guessed the word", word, "!!!")
hangman()

