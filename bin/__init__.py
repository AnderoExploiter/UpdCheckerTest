import random

def number_guessing_game():
    number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    print("====================================")
    print("   Welcome to the Number Guessing Game!")
    print("====================================")
    print("Megasploit: number is: " + str(number))
    print("I have selected a number between 1 and 100.")
    print("Can you guess what it is?\n")

    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts}\nEnter your guess: "))
        attempts += 1

        if guess > number:
            print("Your guess is too high! Try again.\n")
        elif guess < number:
            print("Your guess is too low! Try again.\n")
        else:
            print(f"Congratulations! You guessed the number {number} in {attempts} attempts.")
            break
        if attempts == max_attempts:
            print(f"Sorry, you've reached the maximum number of attempts.")
            print(f"The number was {number}.\n")

    print("Game Over")
    print("====================================")

if __name__ == "__main__":
    number_guessing_game()
