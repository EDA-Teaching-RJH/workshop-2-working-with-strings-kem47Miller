import random

def num(t, p):
    if t > p:
        print("Number too high")
    elif t == p:
        print("Correct!")
    else:
        print("Number too low")
         
def main():
    guess = int(input("Guess a number from 1 to 10: "))
    secret_number = random.randint(1, 10)
    num(guess, secret_number)
    print(f"The actual number was: {secret_number}")

main()  