import random

def start_number_guessing_game():
    random_number = random.randint(1, 20)
    attempts = 0

    while attempts < 3:
        try:
            guess = int(input("Guess the number (Between 1 and 20): "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if guess == random_number:
            print("You did it! Your guess is correct!")
            break
        elif guess < random_number:
            print("Oops! Your guess is too low. Try again.")
        else:
            print("Uh-oh! Your guess is too high. Try a lower number.")

        attempts += 1

    if attempts == 3:
        print("Game over! You did not guess the number within the allowed attempts. The number was", random_number)

# Let's start the game!
start_number_guessing_game()
