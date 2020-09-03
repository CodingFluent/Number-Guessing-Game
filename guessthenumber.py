import random

number = random.randrange(1, 40)
guess = int(input("Guess the number between 1 and 40 : "))

while guess != number:
    if guess < number:
        print ("You need to guess higher. Try again")
        guess = int(input("Guess the number between 1 and 40 : "))
    else:
        print ("You need to guess lower.Try again")
        guess = int(input("Guess the number between 1 and 40 : "))

print ("You have guessed the number correctly!")