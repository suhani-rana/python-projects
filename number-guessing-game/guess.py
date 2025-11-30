import random

def play():
    number = random.randint(1, 50)
    attempts = 0
    print("I have picked a number between 1 and 50. Try to guess it!")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < number:
                print("Try a bigger number.")
            elif guess > number:
                print("Try a smaller number.")
            else:
                print(f"Correct! The number was {number}. Total attempts: {attempts}")
                break

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    play()
