############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
def deal_cards():
    """Returns a random card from the deck"""
    card_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(card_list)
    return random_card

def calculate_score(player_cards):
    """Take a list of cards and return the total score"""
    score = sum(player_cards)
    if score == 21 and len(player_cards) ==2:
        return 0
    if score>21 and 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
    return score

def compare_scores (user_score,computer_score):
    if user_score> 21 and computer_score > 21:
        return 'You went over, both loose'
    elif user_score == computer_score:
        return 'Its a draw'
    elif computer_score == 0:
        return 'You loose, computer has black Jack '
    elif user_score == 0:
        return 'You have Black Jack, You Win!'
    elif computer_score>21:
        return 'You win!'
    elif user_score < computer_score:
        return 'You loose'
    elif user_score>21:
        return 'You went over, You loose'
    else:
        return 'You win!'

def final_data_message(user_cards,computer_cards,user_score,computer_score,):
    print(f'Your cards are: {user_cards}')
    print(f'Your score is: {user_score}')
    print(f'Computer cards are: {computer_cards}')
    print(f'The computer score is: {computer_score}')


def play_game():
    from art_blackJack import logo
    print(logo)
    user_cards = []
    computer_cards = []
    game_over=False
    for _ in range (0,2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    while game_over ==False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'Your cards are: {user_cards}')
        print(f'The total of your cards is {user_score}')
        print(f'The computer card is: {computer_cards[0]}')
        if computer_score == 0 or user_score ==0 or computer_score >21 or user_score>21:
            print(compare_scores(user_score, computer_score))
            final_data_message(user_cards,computer_cards,user_score,computer_score,)
            game_over = True
        else:
            user_should_deal = input('Do you want to draw another card? y/n ')
        while computer_score !=0 and computer_score < 17:
            computer_cards.append(deal_cards())
            computer_score = calculate_score(computer_cards)
        if user_should_deal == 'y':
            user_cards.append(deal_cards())
        else:
            print(compare_scores(user_score, computer_score))
            final_data_message(user_cards, computer_cards, user_score, computer_score, )
            game_over = True

play_game()




#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.