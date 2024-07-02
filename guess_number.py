# Guess the Number game

# Set the secret number
secret_number = 42

# Initialize the number of attempts
attempts = 0

# Welcome the player
print("Welcome to Guess the Number!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")

# Game loop
while True:
    # Ask the player for their guess
    user_guess = input("Enter your guess: ")

    # Check if the input is a valid number
    try:
        user_guess = int(user_guess)
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    # Check if the guess is within the range
    if user_guess < 1 or user_guess > 100:
        print("Invalid input! Please enter a number between 1 and 100.")
        continue

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if user_guess == secret_number:
        print(f" Congratulations! You guessed the number in {attempts} attempts.")
        break

    # Give a hint if the guess is too high or too low
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")