from random import randint

EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS =5

turns = 0
def check_answer(guess,answer,turns):
    """checks answer against guess.Return the number of turns remain"""
    if guess>answer:
        print("To high")

        return  turns -1
    elif guess < answer:
        print("Too low.")
        return -1
    else:
        print(f"You got if! The answer was{answer}.")

# make function to set difficulty.
def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard' : ")
    if level=="easy":
        return  EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("welcome to the Number Guessing Game!")
    print("I'm thingking of a number between 1 and 100.")

    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    turns =set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")


    guess =0
    while guess !=answer:
        print(f"you have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess:"))

        turns=check_answer(guess,answer,turns)

        if turns ==0:
            print("You've run out of guessess, you lose.")
            return
        elif guess != answer:
            print("Guess again...")


game()