import random

playing = True

number = str(random.randint(0,20))



print("I am going to guess a number from 1 and 20 okay! Your job is to guess my number!\nYou win when you get it once, miss 3 times and you lose!")

while playing:
    guess = input("\nWhat is your guess: ")

    if number == guess:
        print(f"\nGood job, the number was indeed {guess}!")
        print("You have won!")
        break
    else:
        print("Try again, your answer is wrong!")
