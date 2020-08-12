from random import randint

print('Welcome to the number guessing game!')

attempts = 0

random_number = randint(0,10)

while attempts != 10:
    attempts += 1
    number_guessed = input("Guess a number 1-10 ")
    if int(number_guessed) > int(random_number):
        print("Your number is too high")
    elif int(number_guessed) < int(random_number):
        print("Your number is too low")
    elif int(number_guessed) == int(random_number):
        print("Congrats!! You guessed the right number")
        print("You took {} tries to guess the right number".format(attempts))
        break
    else:
        print("Please try again")
