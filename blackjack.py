cards = [11, 10, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
import random
from os import system, name
def clear():
    if name == 'nt':
        _ = system('cls')
def initial_cards_user ():
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    list = [card1, card2]
    return list

def sum_initial_cards_user(list):
    s = 0
    for i in list:
        s += i
    if s == 22:
        return 12
    return s
def computer_first_card():
    card = random.choice(cards)
    return card
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play != 'y' and play != 'n':
    play = input("Please press again correctly! Type 'y' or 'n': ")
if play == 'y':
    sum = int(input("Great! How much cash do you have? $"))
while play == 'y' and sum > 0:
    clear()
    bet = int(input("How much you want to bet? $"))
    user_cards = initial_cards_user()
    sum_user = sum_initial_cards_user(user_cards)
    comp_card = computer_first_card()
    print(f"Your cards are {user_cards}, current score = {sum_user}")
    print(f"Computer's first card: {comp_card}")
    ok = 1
    user_win = False
    comp_win = False
    equality = False
    if sum_user == 21:
        print("You win a Blackjack!!!")
        ok = 0
        sum = sum + 3 / 2 * bet
    list_comp = []
    while ok == 1:
        question = input("Type 'y' to get another card, type 'n' to pass: ")
        if question == 'y':
            plus_card = random.choice(cards)
            if plus_card == 11 and sum_user >= 11:
                plus_card = 1
            user_cards.append(plus_card)
            sum_user += plus_card
            print(f"Your cards are {user_cards}, current score = {sum_user}")
            print(f"Computer's first card: {comp_card}")
            if sum_user > 21:
                comp_win = True
                ok = 0
        else:
            list_comp.append(comp_card)
            sum_comp = computer_first_card()
            while sum_comp < 17:
                new_card = random.choice(cards)
                list_comp.append(new_card)
                sum_comp += new_card
            print(f"Computer's final hand: {list_comp}, final score = {sum_comp}")
            if sum_comp > 21:
                user_win = True
                ok = 0

            if sum_user <= 21 and sum_comp <= 21:
                if sum_user > sum_comp:
                    user_win = True
                    comp_win = False
                    ok = 0
                elif sum_user < sum_comp:
                    user_win = False
                    comp_win = True
                    ok = 0
                else:
                    equality = True
                    ok = 0

    if equality == True:
        print("You obtained a draw!")
    elif comp_win == True:
        print("You lost!")
        sum = sum - bet

    else:
        print("You win!!!")
        sum = sum + bet
    if sum > 0:
        play = input(f"You have now a total of {sum}$. Do you want to play again? Type 'y' or 'n': ")
        while play != 'y' and play != 'n':
            play = input("Please press again correctly! Type 'y' or 'n': ")
        if play == 'n':
            print(f"You left out with total sum of {sum}$")
    else:
        print("Unfortunately, you left casino with 0$. Try again next time!")
