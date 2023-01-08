import random
from brain_games.scripts.brain_games import main

from brain_games.scripts.brain_components import start_string, check_answers


name = main()

start_string("What is the result of the expression?")


operation = random.choice(['+', '-', '*'])
count = 0
while (count < 3):
    num1 = random.randint(0,100)
    num2 = random.randint(0,100)
    print("Question: " + str(num1) + operation + str(num2) + '\n')
    if (operation == '+'):
        right_answer = num1 + num2
    elif (operation == '-'):
        right_answer = num2 - num1
    elif (operation == '*'):
        right_answer = num1 * num2
    answer = input("Your answer: ")
    if check_answers(answer, right_answer, name) == False:
        break
    count += 1
print(f"Congratulations, {name}!\n")