import random


# ---------------------------------------------------------
# Function 1: Display the game instructions
# ---------------------------------------------------------
def show_instructions():
    """
    Display a welcome message and explain the rules.

    TODO:
    - Welcome the player.
    - Explain that the secret contains 4 different digits.
    - Explain what Bulls and Cows mean.
    """
    pass


# ---------------------------------------------------------
# Function 2: Generate the secret number
# ---------------------------------------------------------
def generate_secret():
    """
    Generate and return a list of 4 unique random
    integers between 0 and 9.

    Example:
        [3, 7, 1, 9]

    Hint:
        Use random.randint() and a while loop.
    """
    pass


# ---------------------------------------------------------
# Function 3: Get the player's guess
# ---------------------------------------------------------
def get_guess():
    """
    Ask the player to enter 4 integers, one at a time.

    Store the numbers in a list and return that list.

    Example:
        Enter digit 1: 3
        Enter digit 2: 5
        Enter digit 3: 1
        Enter digit 4: 9

    Returns:
        [3, 5, 1, 9]
    """
    pass


# ---------------------------------------------------------
# Function 4: Check for duplicate numbers
# ---------------------------------------------------------
def has_duplicates(numbers):
    """
    Check whether a list contains duplicate numbers.

    Return True if duplicates exist.
    Return False otherwise.

    Examples:
        has_duplicates([1, 2, 3, 2]) -> True
        has_duplicates([1, 2, 3, 4]) -> False
    """
    pass


# ---------------------------------------------------------
# Function 5: Check whether the guess is valid
# ---------------------------------------------------------
def is_valid_guess(guess):
    """
    Return True if:
    - The list contains exactly 4 numbers.
    - All numbers are between 0 and 9.
    - There are no duplicates.

    Return False otherwise.

    Examples:
        is_valid_guess([1, 2, 3, 4]) -> True
        is_valid_guess([1, 2, 2, 4]) -> False
        is_valid_guess([1, 2, 3, 12]) -> False

    Hint:
        You can call has_duplicates() inside this function.
    """
    pass


# ---------------------------------------------------------
# Function 6: Count Bulls
# ---------------------------------------------------------
def count_bulls(secret, guess):
    """
    Count and RETURN how many digits are correct
    AND in the correct position.

    Example:
        secret = [1, 2, 3, 4]
        guess  = [1, 5, 3, 6]

        Returns: 2
    """
    pass


# ---------------------------------------------------------
# Function 7: Count Cows
# ---------------------------------------------------------
def count_cows(secret, guess):
    """
    Count and RETURN how many digits exist in the
    secret but are in the WRONG position.

    Example:
        secret = [1, 2, 3, 4]
        guess  = [4, 3, 5, 1]

        Returns: 3

    Remember:
        A digit cannot count as both a Bull and a Cow.
    """
    pass


# ---------------------------------------------------------
# Function 8: Display the results
# ---------------------------------------------------------
def show_result(bulls, cows):
    """
    Print the number of Bulls and Cows.

    Example:
        show_result(2, 1)

    Output:
        Bulls: 2
        Cows: 1
    """
    pass


# ---------------------------------------------------------
# Function 9: Check whether the player won
# ---------------------------------------------------------
def has_won(bulls):
    """
    Return True if the player has 4 Bulls.
    Return False otherwise.

    Examples:
        has_won(4) -> True
        has_won(2) -> False
    """
    pass


# ---------------------------------------------------------
# Function 10: Display the final message
# ---------------------------------------------------------
def show_final_message(attempts):
    """
    Congratulate the player and display the total
    number of attempts.

    Example:
        Congratulations!
        You guessed the secret in 6 attempts!
    """
    pass


# =========================================================
# MAIN GAME
# =========================================================

def main():

    show_instructions()

    secret = generate_secret()

    attempts = 0
    won = False

    while not won:

        print()
        print("--------------------------")
        print("Attempt:", attempts + 1)

        guess = get_guess()

        # Keep asking until the player enters a valid guess.
        while not is_valid_guess(guess):
            print("Invalid guess! Please try again.")
            guess = get_guess()

        attempts += 1

        bulls = count_bulls(secret, guess)
        cows = count_cows(secret, guess)

        show_result(bulls, cows)

        won = has_won(bulls)

    show_final_message(attempts)


# Start the game
main()