
# Import the Flask class to create our web app
from flask import Flask
# Import the random module to generate a random number for the game
import random

# Generate a random integer between 0 and 9 (inclusive) and store it
random_number = random.randint(0, 9)


# Initialize the Flask application using the current module name (__name__)
app = Flask(__name__)

# Define what happens when a user visits the main homepage ("/")
@app.route('/')
def home():
    # Return an HTML string containing a heading and an introductory Giphy GIF
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

# Define a dynamic route that captures an integer from the URL (e.g., /5) and passes it as 'guess'
@app.route("/<int:guess>")
def guess_number(guess):
    # Check if the user's guessed number is higher than the generated random number
    if guess > random_number:
        # Return purple text saying "Too high" along with a reaction GIF
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
               
    # Check if the user's guessed number is lower than the generated random number
    elif guess < random_number:
        # Return red text saying "Too low" along with a reaction GIF
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
               
    # If the guess is neither higher nor lower, it must be the correct number!
    else:
        # Return green text celebrating the win along with a success GIF
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"

# Check if this script is being run directly (not being imported as a module elsewhere)
if __name__ == "__main__":
    # Start the local Flask development server with debug mode enabled
    # Debug mode automatically reloads the server whenever you save changes to your code
    app.run(debug=True)
