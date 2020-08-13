from random import randint



def start_game():
    print('Welcome to the number guessing game!')
    attempts = 0
    random_number = randint(1,10)
    while True:
        attempts += 1
        try:
            guess = int(input("Guess a number 1-10  "))
        except ValueError:
            print("Oops, thats not a number")
        else:
            if guess > 10:
                print("Whoops thats not a number 1-10!")
            elif guess > random_number:
                print("It's lower!")
            elif guess < random_number:
                print("It's higher!")
            elif guess == random_number:
                print("Congrats!! You guessed the right number")
                print("You took {} tries to guess the right number.".format(attempts))
                ask = input("Would you like to play again?  (Yes/No)  ")
                if ask.upper() == "YES":
                    start_game()
                elif ask.upper() == "NO":
                    print("Thanks for playing!")
                    quit()
                else:
                    quit()
start_game()
