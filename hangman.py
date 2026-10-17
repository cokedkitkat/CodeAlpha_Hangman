"""
CodeAlpha Task 1: Hangman Game
------------------------------
The computer picks a secret word. You guess one letter at a time.
You are allowed 6 wrong guesses. Guess the word before that and you win!
"""

import random

# A small list of 5 words the computer can choose from
WORDS = ["python", "banana", "laptop", "garden", "rocket"]

MAX_WRONG_GUESSES = 6


def show_word(secret_word, guessed_letters):
    """Show the word with underscores for letters not guessed yet.
    Example: if the word is 'python' and you guessed 'p' and 'o' -> 'p _ _ _ o _'
    """
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    secret_word = random.choice(WORDS)   # computer picks a random word
    guessed_letters = []                 # every letter the player has tried
    wrong_guesses = 0                    # how many mistakes so far

    print("=" * 35)
    print("       WELCOME TO HANGMAN!")
    print("=" * 35)
    print(f"I have picked a word with {len(secret_word)} letters.")
    print(f"You can make {MAX_WRONG_GUESSES} wrong guesses. Good luck!\n")

    # Keep playing until the player wins or runs out of guesses
    while wrong_guesses < MAX_WRONG_GUESSES:
        print("Word:", show_word(secret_word, guessed_letters))
        print("Letters tried:", " ".join(sorted(guessed_letters)) or "none yet")
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")

        guess = input("Guess a letter: ").strip().lower()

        # Check that the input is exactly one letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please type just ONE letter (a-z).\n")
            continue

        # Check that the letter was not already tried
        if guess in guessed_letters:
            print("You already tried that letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Nice! That letter is in the word.\n")
        else:
            wrong_guesses += 1
            print("Sorry, that letter is not in the word.\n")

        # Did the player find every letter?
        if all(letter in guessed_letters for letter in secret_word):
            print("Word:", show_word(secret_word, guessed_letters))
            print("\n*** YOU WIN! Great job! ***")
            return

    print(f"Game over! The word was: {secret_word}")


# Ask if the player wants to play again after each round
if __name__ == "__main__":
    while True:
        play_hangman()
        again = input("\nPlay again? (yes/no): ").strip().lower()
        if again not in ("yes", "y"):
            print("Thanks for playing. Goodbye!")
            break
        print()
