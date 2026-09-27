import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def deal_card(hand):
    card = random.choice(cards)
    hand.append(card)
    print(hand)


def calculate_score(list1):
    score = sum(list1)
    if len(list1) == 2 and score == 21:
        return 0
    while 11 in list1 and score > 21:
        list1.remove(11)
        list1.append(1)
        score = sum(list1)
    return score


def compare_score(x , y):
    message = ""
    if x > y:
        message = "Computer wins"
        return message
    if y > x:
        message = "Player wins"
        return message
    if y == x:
        message = "Draw"
        return message

def play_game():
    user_cards = []
    computer_cards = []
    user_total = 0
    computer_total = 0
    game_on = True

    print(art.logo)
    print('Your first card is')
    deal_card(user_cards)
    print('Dealers first card is')
    deal_card(computer_cards)
    print('Your hand is')
    deal_card(user_cards)

    while game_on == True:
        user_total = calculate_score(user_cards)
        if user_total == 0:
            print('You have Blackjack, you win!')
            game_on = False
            break
        if user_total > 21 :
            print("Player bust")
            game_on = False
            break
        computer_total = 0
        for card in computer_cards:
            computer_total += card

        hit = input("Do you want to get another card? Y/N ").lower()
        if hit == "y":
            card = random.choice(cards)
            user_cards.append(card)
            print(user_cards)


        if hit == "n":
            game_on = False
            deal_card(computer_cards)
            computer_total = calculate_score(computer_cards)
            if computer_total == 0:
                print('Computer has Blackjack, you lost.')
                game_on = False
                break
            while computer_total < 17:
                deal_card(computer_cards)
                computer_total = calculate_score(computer_cards)
            if computer_total > 21:
                print("Dealer bust, you win")
                break
            compare = compare_score(computer_total, user_total)
            print(compare)
            print(f'Your cards are {user_cards}, your total is {user_total}.\n'
                    f'Dealers cards are {computer_cards}, Dealers total is {computer_total}.')


while input("Do you want to play Blackjack? Y/N: ").lower() == 'y':
    print("\n"*20)
    play_game()

