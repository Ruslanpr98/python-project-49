import sys
import random

game_name = sys.argv[0]

def start_string(welcome_string):
    print(welcome_string)


def check_answers(answer, right_answer, name):
    if (answer != right_answer):
        print(f"{answer} is wrong answer ;(. Correct answer was {right_answer}.\n Let's try again {name}!\n")
        return False
    else:
        print("Correct!\n")

def game_logic(count, question, answer, right_answer, name, operation=None):
    count = 0
    while (count < 3):
        if (game_name == "brain_even"):
            num = random.randint(0,100)
            print("Question: " + question + '\n')
            if (num % 2 == 0):
                right_answer = 'yes'
            else:
                right_answer = 'no'
            answer = input("Your answer: ")
            print('\n')
            if check_answers(answer, right_answer, name) == False:
                count = 0
            count += 1
        if (game_name == "brain_calc"):
            num1 = random.randint(0,100)
            num2 = random.randint(0,100)
            operation = random.choice(operation)
            print("Question: " + question + '\n')
            if (operation == '+'):
                right_answer = num1 + num2
            elif (operation == '-'):
                right_answer = num1 - num2
            elif (operation == '*'):
                right_answer = num1 * num2
            if check_answers(answer, right_answer, name) == False:
                break
            count += 1
    print(f"Congratulations, {name}!\n")
        
    