#!/usr/bin/env python3
from brain_games.cli import welcome_user
#from brain_games.scripts.brain_even import game_logic


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    return name

def greet():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    return name


if __name__ == "__main__":
    main()
