import ascii_art
import random


STAGES = ascii_art.STAGES
# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"Word: {display_word}")
    print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
    print(f"Mistakes left: {(len(STAGES) - 1) - mistakes}\n")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations, you saved the snowman!")
            return

        # Get user guess
        guess = input("Guess a letter: ").lower().strip()

        # Validate input
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1

    # Player lost while loop ends
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game Over! The word was: {secret_word}")