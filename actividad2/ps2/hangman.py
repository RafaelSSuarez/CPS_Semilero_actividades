# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    
    cont_coicidencias=0
    for A in letters_guessed:
        for B in secret_word:
            if A==B:
                cont_coicidencias=cont_coicidencias+1
            else:
                cont_coicidencias=cont_coicidencias
    if cont_coicidencias==len(secret_word):
        adivinada=True
    else:
        adivinada=False
    return(adivinada)




def get_guessed_word(secret_word, letters_guessed):
    salida="_ "*len(secret_word)
    for C in letters_guessed:
        cont_posicionstring=0  
        for D in secret_word:
            if C==D:
                if cont_posicionstring==0:
                    salida=C+salida[cont_posicionstring+1:len(salida)]
                else:
                    salida=salida[0:cont_posicionstring]+C+salida[cont_posicionstring+1:len(salida)]
            cont_posicionstring=cont_posicionstring+2   
    return(salida)



def get_available_letters(letters_guessed):
    available=string.ascii_lowercase
    for E in letters_guessed:
        cont_available=0
        for F in available:
            if F==E:
                if cont_available==0:
                    available=available[cont_available+1:len(available)]
                else:
                    available=available[0:cont_available]+available[cont_available+1:len(available)]        
            cont_available=cont_available+1   
    return(available)
    
    

def hangman(secret_word):
    largo=len(secret_word)
    intentos=6
    advertencias=3
    revisar=False
    letra="0"
    print("Welcome to the game Hangman!\nI am thinking of a word that is",largo,"letters long.\n__________\n\n")
    #while intentos>0:
    print("You have",intentos,"guesses left.\nAvailable letters: ",get_available_letters(letra))
    agrego_letra=input("Please guess a letter:")
    revisar=str.isalpha(agrego_letra)
    if revisar:
        letra=letra+agrego_letra
    else:
        print("inserte algo válido")
            
    
    print("look: ",get_guessed_word(secret_word, letra))
    print("You have",intentos,"guesses left.\nAvailable letters: ",get_available_letters(letra))
   
    
    
    
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
