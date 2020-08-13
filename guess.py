from random import randint

print('Welcome to the number guessing game!')

def start_game():
    attempts = 0
    random_number = randint(1,10)
    while True:
        guess = input("Guess a number 1-10  ")
        attempts += 1
        try:
            int(guess)
        except ValueError:
            print("Oops, thats not a number")
            continue
        if int(guess) > random_number:
            print("It's lower")
        elif int(guess) < random_number:
            print("It's higher!")
        elif int(guess) == random_number:
            print("Congrats!! You guessed the right number")
            print("You took {} tries to guess the right number.".format(attempts))
            ask = input("Would you like to play again?  (Yes/No)  ")
            if ask.upper() == "YES":
                start_game()
            elif ask.upper() == "NO":
                print("Thanks for playing!")
                quit()
            else:
                print("I'll take that as a yes!")
                continue
start_game()
