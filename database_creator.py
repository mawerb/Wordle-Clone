from wordle import Wordle

def main():
    input_file_path = "wordsource.txt"
    output_file_path = "wordleData.txt"
    valid_words = []

    with open(input_file_path, "r") as data:
        for line in data.readlines():
            word = line.strip()
            if len(word) == Wordle.WORD_LENGTH:
                valid_words.append(word)

    with open(output_file_path, "w") as data:
        for word in valid_words:
            data.write(word + "\n")

    print(f"Found {len(valid_words)} {Wordle.WORD_LENGTH}-letter words")

if __name__ == "__main__":
    main()