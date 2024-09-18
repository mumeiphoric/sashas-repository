import random

def playgame():
    low = 1
    high = 100
    attempts = 0

    num = random.randint(low, high)

    print(f"CAN YOU GUESS A NUMBER BETWEEN {low} AND {high}??")

    while True:
        try:
            guess = int(input(f"Guess a number! --> "))
            attempts += 1
            if guess < num:
                print("The number is higher!")
            elif guess > num:
                print("The number is lower!")
            elif guess > high or guess < low:
                print("Please enter a number within the range!")
            else:
                print(f"YOU'RE THE GOAT!!! (˶˃⤙˂˶) ")
        except ValueError:
            print("ERROR! Guess a valid number.")

if __name__ == "__main__":
    playgame()


