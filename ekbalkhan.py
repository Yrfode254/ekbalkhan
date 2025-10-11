import random

number = random.randint(1, 5)
guess = int(input("Guess 1-5: "))

if guess == number:
    print("Correct!")
else:
    print(f"Wrong! It was {number}")