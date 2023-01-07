import random
from brain_games.scripts.brain_games import main
    

name = main()
print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
count = 0
right_answer = ''
while (count < 3):
    number = random.randint(0,100)
    print("Question: " + str(number) + '\n')
    if (number % 2 == 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    answer = input("Your answer: ")
    print('\n')
    if (answer != right_answer):
        print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}.\n Let's try again {name}!\n")
        count = 0
    else:
        print("Correct!\n")
    count += 1
print(f"Congratulations, {name}!\n")


