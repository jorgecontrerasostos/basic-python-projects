import random

def main():
    number_to_guess = random.randint(1, 10)
    num = 0

    while num != number_to_guess:
        try:
            num = int(input("Enter a number from one to 10\n"))
            if num > number_to_guess:
                print("Too high")
            elif num < number_to_guess:
                print("Too Low")
            else:
                print("Correct")
        except ValueError:
            print("Not a number")
if __name__ == "__main__":
    main()
