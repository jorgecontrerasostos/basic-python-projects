import random

def main():
    number_to_guess = random.randint(1, 10)
    num = 0

    while num != number_to_guess:

        num = int(input("Enter a number from one to 10\n"))
        if not isinstance(num, int):
            print("Not a number")
        if num > number_to_guess:
            print("Too high")
        elif num < number_to_guess:
            print("Too Low")
        else:
            print("Correct")

if __name__ == "__main__":
    main()
