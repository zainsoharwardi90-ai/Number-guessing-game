
secret_number = 37 
guess = None
attempts = 0

print("Guess the secret number between 1 and 50!")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low. Try again.")
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
