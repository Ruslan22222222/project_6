import random
import os
from art import logo

def deal_card():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 10, 10, 10]
    card = random.choice(cards)
    return card

def calculating_score(cards):
    if sum(cards) > 21 and len(cards) > 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over! U lose!"
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "U lose!"
    elif user_score == 0:
        return "U win!! ! "
    elif computer_score > 21:
        return "U win!"
    elif user_score > 21:
        return "U lose!"
    elif user_score > computer_score:
        return "U win!"
    else:
        return "U lose!"

def play_game():
    print(logo)
    user_cards = []
    computer_cards =[]
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not is_game_over:
        user_score = calculating_score(user_cards)
        computer_score = calculating_score(computer_cards)

        print(f"   Your cards {user_cards} your current score {user_score}")
        print(f"Computer's card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal = input("Do u want to get another card? Type 'y or 'n' to pass? ")
            if should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculating_score(computer_cards)
    
    print(f"        Your final hand: {user_cards}, final score: {user_score}")
    print(f"        Computer's final hand {computer_cards},, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play again? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()

    





    







    







 






    













