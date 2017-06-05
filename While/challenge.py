import random

highest = 10
answer = random.randint(1, highest)
guess = None
print("Please guess a number between 1 and {}: ".format(highest))

while guess != answer:

    guess = int(input())
    if guess < answer:
        print("Please guess higher")
    elif guess > answer: #guess must be greater than number
        print("Please guess lower")
    else:
        print("Well done, you guessed it. {}".format(answer))

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else: #guess must be greater than number
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well donw, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")












