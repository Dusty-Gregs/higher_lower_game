import random
from art import logo
from art import vs
from game_data import data
import os



def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


list_choice = []

def check_answer(A, B, a_value, b_value, answer, user_score):
    #checks answer and increases score if correct
    if a_value > b_value and answer == A:
        return user_score + 1
    elif a_value > b_value and answer == B:
        clear_terminal()
        print(f"Sorry, that's wrong, Final score: {user_score}")
        gameover = True
        return
    elif b_value > a_value and answer == B:
        return user_score + 1
    elif b_value > a_value and answer == A:
        clear_terminal()
        print(f"Sorry, that's wrong, Final score: {user_score}")
        gameover = True
        return
    else:
        print()

def add_to_list():
    #Adds random choice to list
    list_choice.append(random.choice(data))

def game():
    #start of game, adds initial 2 to list
    add_to_list()
    add_to_list()
    A = list_choice[-1]
    B = list_choice[-2]
    a_value = A['follower_count']
    b_value = B['follower_count']

    print(logo)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.\r")
    print(vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B':").upper()
    
    user_score = 0
    gameover = False

    while not gameover:
        check_answer(A, B, a_value, b_value, answer, user_score)

        add_to_list()
        A = list_choice[-1]
        B = list_choice[-2]

        clear_terminal()

        print(logo)
        print(f"You're right! Current score: {user_score}.")
        print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.\r")
        print(vs)
        print(f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")
        answer = input("Who has more followers? Type 'A' or 'B':").upper()

game()