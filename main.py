import random
guess = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("===== NUMBER GUESSING GAME =====\n")
user_guess = int(input("Enter your guess: "))
chances = 0
while True:
    if user_guess > guess:
        print(f"{user_guess} is greater than original number")
        user_guess = int(input("Enter your guess: "))
    elif user_guess < guess:
        print(f"{user_guess} is less than original number")
        user_guess = int(input("Enter your guess: "))
    elif user_guess == guess:
        print("Your guess is correct")
        break













