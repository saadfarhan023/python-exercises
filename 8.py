from random import randint

computer = randint(1, 100)
guesses = 0

while True:
    human = int(input("Enter your guess: "))
    guesses += 1
    if human > computer:
        print("lower")
    elif human < computer:
        print("higher")
    else:
        print("you won", computer)
        print("total guesses", guesses)