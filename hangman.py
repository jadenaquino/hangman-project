# modification 1. the 20 words
import random
from words import words
from HANGMAN_PICS import lives_visual_dict
import string

# modification 2. adding the hangman
HANGMAN_PICS = {
6: '''+---+
         |
         |
         |
        ===''', 
5: ''' +---+
      O   |
          |
          |
        ===''',
4: '''+---+
      O   |
      |   |
          |
       ===''', 
3: '''+---+
      O   |
     /|   |
          |
       ===''', 
2: '''+---+
      O   |
     /|\  |
          |
       ===''', 
1:'''+---+
     O   |
    /|\  |
    /    |
       ===''', 
0: '''+---+
      O   |
     /|\  |
     / \  |
      ==='''
}


def get_valid_word(words):
    word = random.choice(words)
    while  'Kwantlen' in word or 'Rai ' in word or 'Zimmerman' in word or '-' in word:
        word = random.choice(words)

    return word.upper()

def hangman():
    global word
    word = get_valid_word(words)
    global word_letters 
    word_letters = set(word)
    global alphabet
    alphabet = set(string.ascii_uppercase)
    global used_letters
    used_letters = set()
    
lives = 6

hangman()


while len(word_letters) > 0 and lives > 0:
    
    
    print("You have ", lives, "lives left and you used these  letters: ", ' '.join(used_letters))
    
    
    
    word_list = [letter if letter in used_letters else '-' for letter in word ]
    print(lives_visual_dict[lives])
    print("Current word: ", ' '.join(word_list))
#modification 4 adding the delay timer
    user_letter = input("Please type a letter: ").upper()
    import time
    time.sleep(1) #sleep for 1 second
#modification 5 my unique messeges.
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        print("Great job the letter was correct.")
        if user_letter in word_letters:
            word_letters.remove(user_letter)

        else:
            lives = lives - 1
            print("Dude really? your letter was wrong! ")

    elif user_letter in used_letters:
        print("Bruh you already used that. Try again")
    
    else:
        print("Invalid. Please put a letter not a number")


if lives == 0:
    print(lives_visual_dict[lives])
    print("Damn you died that's tuff. The word was ", word)
else:
    print("Sheesh you guessed the word", word, "!!")

hangman()


#modification 3 asking the user if they want to play again if they have won or died.
def user_option():
    user_choice = " "
    while user_choice != "y" or "n":
        user_choice = input("Would you like to play? 'Y' or 'N': ")
        if user_choice == "y":
            hangman()
            continue
        elif user_choice == "n":
            return "Game Over!"
        else:
            print("That is an invalid response.")

result = user_option()
print(result)




    # modification 6 adding a message if the player says N.
print("Thanks for playing sucker, hope to you again soon :)")

"""
user_choice = " "
    while user_choice != "N" or "Y":
        user_choice = input("Would you like to play? Y or N: ").upper()

        if user_choice == "Y":
            return hangman()
            
        
        elif user_choice == "N":
            return "Thanks for playing the game."
        
            
        #else:
            #print("that is an invalid answer!")
 """           






        












