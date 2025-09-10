import random

def guess_the_number():
    print(" Welcome to the Guess the Number Game! ")
    print("I have picked a number between 1 and 100.")
    print("Can you guess it? ")

    # Generate random number
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try a hgher number ")
            elif guess > number_to_guess:
                print("Too high! Try a lower number )
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts")
                break

        except ValueError:
            print("Please enter a valid number!")

# Run the game
guess_the_number()
