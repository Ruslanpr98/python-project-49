import random
from brain_games.scripts.brain_games import main

from brain_games.scripts.brain_components import start_string, check_answers, game_logic


name = main()

start_string("Answer \"yes\" if the number is even, otherwise answer \"no\".")
count = 0
right_answer = ''
answer = ''
num = 0
question = f"{num}"
while (count < 3):
    number = random.randint(0,100)
    print("Question: " + str(number) + '\n')
    if (number % 2 == 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    answer = input("Your answer: ")
    print('\n')
    if check_answers(answer, right_answer, name) == False:
        count = 0
    count += 1
print(f"Congratulations, {name}!\n")
#game_logic(count, question, answer, right_answer, name)



