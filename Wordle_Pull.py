from flask import Flask, request, jsonify, render_template
from wordle import Wordle

import random

app = Flask(__name__) #initializes flask app

#load word set
def load_words(filepath): #used to create a unique set of words from wordleData.txt
    word_set = set()
    with open(filepath,'r') as file:
        for line in file.readlines():
            word = line.strip().upper()
            word_set.add(word)
        return word_set

word_set = load_words("wordleData.txt")
secret_word = random.choice(list(word_set)) #gets a random word from the word array
wordle = Wordle(secret_word) # Initializes class object wordle


@app.route("/")#routes to homepage
def home():
    return render_template('home.html') #main page (take note, webpage must be in template folder)

@app.route('/guess', methods = ["POST"]) #routes to guess page
def guess():
    guess_word = request.json.get("guess").upper() #pulls json text of inputted user guess on frontend
    if len(guess_word) != wordle.WORD_LENGTH:
        return jsonify({"error":"Invalid Length"}), 400
    if guess_word not in word_set:
        return jsonify({"error":"Invalid Word"}), 400

    #creates object variables
    wordle.attempt(guess_word)
    results = wordle.guess(guess_word)
    is_solved = wordle.is_solved
    remaining_attempts = wordle.remaining_attempts
    can_attempt = wordle.can_attempt

    #returns json data to frontend
    return jsonify({
        "results" : [letter.to_dict() for letter in results], #letter.to_dict() works because results is a letterstate object
        "is_solved" : is_solved,
        "remaining_attempts" : remaining_attempts,
        "can_attempt" : can_attempt
    })

if __name__ == "__main__":
    app.run(debug=True)
