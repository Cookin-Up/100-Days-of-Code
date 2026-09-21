import random
import art

print(art.logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

secret_number =  random.randint(1, 100)
print(f"Secret number is ")
guess = 0

difficulty = input("Please choose a diffulty. Type 'easy' or 'hard' ").lower()
attempts = 0

if difficulty == "hard":
    attempts = 5
    print(f"you have {attempts} attempts remaining")
elif difficulty == "easy":
    attempts = 10
    print(f"you have {attempts} attempts remaining")

while attempts > 0:
    guess = int(input("Please enter a guess: "))
    if guess == secret_number:
        print(f"You win, secret number was {secret_number}")
        break
    elif guess < secret_number:
        attempts = attempts - 1
        print(f"Sorry that wasn't the number, you are too low, {attempts} left ")
    elif guess > secret_number:
        attempts = attempts - 1
        print(f"Sorry that wasn't the number, you are too high, {attempts} left ")

if attempts == 0 and guess != secret_number:
    print(f"secret_number was {secret_number}")