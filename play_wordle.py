from wordle import Wordle
from colorama import Fore
import random

def display_results(wordle: Wordle):
    print("\nYour Results So Far!")
    print(f"Remaining Attempts {wordle.remaining_attempts}.\n")

    lines = []

    for word in wordle.attempts:
        result = wordle.guess(word)
        colored_result_str = convert_result_into_color(result)
        lines.append(colored_result_str)
    for bar in range(wordle.remaining_attempts):
        lines.append(" ".join(list("_" * wordle.WORD_LENGTH)))

    draw_box_around(lines, 1, wordle.WORD_LENGTH)

def draw_box_around(content, pad, word_length):

    content_length = (word_length*2-1) + pad * 2
    top_border = "┌" + ("─" * content_length) + "┐"
    bottom_border = "└" + ("─" * content_length) + "┘"


    print(top_border)
    for line in content:
        print(f"│{" " * pad}{line}{" " * pad}│")
    print(bottom_border)

def convert_result_into_color(result):
    result_with_color = []

    for letter in result:
        if letter.is_in_position:
            color = Fore.GREEN
        elif letter.is_in_word:
            color = Fore.YELLOW
        else:
            color = Fore.LIGHTWHITE_EX

        colored_letter = color + letter.character + Fore.RESET
        result_with_color.append(colored_letter)

    return " ".join(result_with_color)

def random_word(data):
    word_set = set()

    with open(data, "r") as data:
        for line in data.readlines():
            word = line.strip().upper()
            word_set.add(word)

    return word_set

def main():
    print("Welcome to Wordle!")

    word_set = random_word("wordleData.txt")
    secret = random.choice(list(word_set))
    wordle = Wordle(secret)

    while wordle.can_attempt:
        x = input("Type your guess: ")

        if len(x) != wordle.WORD_LENGTH:
            print(Fore.RED + f"Must be of {wordle.WORD_LENGTH} characters long." + Fore.RESET)
            continue

        if x.upper() not in word_set:
            print(Fore.RED + f"{x} is not a valid word." + Fore.RESET)
            continue

        wordle.attempt(x)
        display_results(wordle)


    if wordle.is_solved:
        print("You have guessed the word!")
    else:
        print("You failed to solve the puzzle.")
        print(f"The secret word was: {secret}")



if __name__ == "__main__":
    main()