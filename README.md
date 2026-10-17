# CodeAlpha_Hangman

A simple text-based Hangman game written in Python, built as **Task 1** of the CodeAlpha Python Programming Internship.

## What it does

The computer secretly picks a word. You try to guess it one letter at a time. Every wrong guess brings you closer to losing, and you are allowed **6 wrong guesses**. Guess all the letters before that and you win!

## Features

- Picks a random word from a list of 5 words
- Shows the word as blanks (for example `_ a _ _ e _`) and reveals letters as you guess them
- Shows the letters you have already tried
- Counts how many wrong guesses you have left
- Checks your input (only one letter at a time, no repeats)
- Lets you play again after each round

## How to run

1. Install Python 3 from [python.org](https://www.python.org/downloads/) if you don't have it.
2. Download `hangman.py` from this repository.
3. Open a terminal in the folder with the file and run:

```
python hangman.py
```

## Example

```
Word: _ _ _ _ _ _
Letters tried: none yet
Wrong guesses left: 6
Guess a letter: a
Nice! That letter is in the word.
```

## Concepts used

`random` module, `while` loops, `if-else` conditions, strings and lists.

## Author

Made by Yasin as part of the CodeAlpha Python Programming Internship.
