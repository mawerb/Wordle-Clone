import string

WORD_LENGTH = 5 # allow for easy word length manipulation

def read_dictionary(file_name):

    with open(file_name, 'r') as valid_words: #open valid word dictionary
        dictionary_list = valid_words.readlines() #read all words in dictionary

        new_dictionary_list = [word.strip().lower() for word in dictionary_list]

    return new_dictionary_list # a list of strings with lowercase letters

def enter_a_word (word_type, num_letters):

    a_word = input(f"Enter the {num_letters}-letter {word_type} word: ").lower().split()[0] #GET user input and lowercase

    return a_word  # return lowercase word

def is_it_a_word (input_word, dictionary_list):
    is_word = True # initialize bool variable as True, only need to check if word is not in list

    if input_word not in dictionary_list: # Check if word isn't in dictionary
        is_word = False

    return is_word # Return word validity

def enter_and_check(word_type, dictionary_list):

    in_word = enter_a_word(word_type, WORD_LENGTH) # Ask user for input using enter_a_word function
    in_dict = is_it_a_word(in_word, dictionary_list)  # Check word validity using is_it_a_word func
    length = len(in_word)# Check word length

    while (not in_dict) or (length != WORD_LENGTH): #loop until word is valid
        print(f'\nYou entered a {length}-letter word that is {"" if in_dict else "not "}in '
              f'the dictionary. \nPlease try again!\n') #Error output depending on errors.

        in_word = enter_a_word(word_type, WORD_LENGTH)

        in_dict = is_it_a_word(in_word, dictionary_list)
        length = len(in_word)


    return in_word # a string - valid input word

def compare_words (player, secret):
    global remaining_alphabet
    global in_secret_word_correct_spot
    global in_secret_word_somewhere
    global not_in_secret_word

    final = '' # initialize final variable as empty string
    in_correct_spot = 0 # initialize correct_spot to 0 and int

    for char in range(len(secret)): # check each character in secret if player char is in right spot

        if secret[char] == player[char]: # is char at index same as char at player?
            in_correct_spot += 1
            final += player[char]

            if player[char] in remaining_alphabet:
                remaining_alphabet.remove(player[char]) # only remove char if in remaining_alphabet

            if player[char] not in in_secret_word_correct_spot: # only append if char not already known
                in_secret_word_correct_spot.append(player[char])

        elif player[char] in secret: # is player char at some index in secret?
            final += f"({player[char]})"

            if player[char] in remaining_alphabet:
                remaining_alphabet.remove(player[char])

            if player[char] not in in_secret_word_somewhere: # only append if char not already known
                in_secret_word_somewhere.append(player[char])

        else:   # no cases met
            final += "_"

            if player[char] in remaining_alphabet:
                remaining_alphabet.remove(player[char])

            if player[char] not in not_in_secret_word: # only append if char not already known
                not_in_secret_word.append(player[char])

    return final, in_correct_spot # returns a string and an integer


# Main Game Code
print('Welcome to the Wordle 2.0!')

alphabet_string = string.ascii_lowercase # create a string of all lowercase letters

# Initializes the lists
remaining_alphabet = list(alphabet_string)
in_secret_word_correct_spot = []
in_secret_word_somewhere = []
not_in_secret_word = []

words_list = read_dictionary("project4_dictionary.txt") # read dictionary list from file

print("\nPlayer 1 UI:\n")
secret_word = enter_and_check('secret', words_list) # GET secret word

attempts = 0 # set to 0 to show user has not made any attempts
N = int(input("Max Attempts:")) # GET max attempts

if N > 0: # only print player 2 UI if there are any attempts
    print("\nPlayer 2 UI:")

while attempts < N:

    attempts += 1 #Counter

    print(f"\nEnter your attempt #{attempts}:")

    player_word = enter_and_check("secret",  words_list) #ask user for new word
    final_word, letter_in_the_right_spot = compare_words(player_word, secret_word) #compare words

    #Print statements for outputs :P
    print(f"\nletter in the right spot: {letter_in_the_right_spot}"
          f"\nYou guessed letters of the secret_word: {final_word}\n")
    print(f"Previously attempted letters that are in the correct spot of secret_word:"
          f"\n{in_secret_word_correct_spot}")
    print(f"Previously attempted letters that are in some spot of secret_word:"
          f"\n{in_secret_word_somewhere}")
    print(f"Previously attempted letters that are not in the secret_word:"
          f"\n{not_in_secret_word}")
    print(f"Remaining letters of the alphabet that have not been tried:"
          f"\n{remaining_alphabet}")

    if player_word == secret_word: #winning case
        print(f"\nCongrats you won using {attempts} attempt(s)")
        break

    elif attempts == N: #user used all attempts and hasn't won
        print(f"\nYou already used #{attempts} attempts. Better luck tomorrow!")
