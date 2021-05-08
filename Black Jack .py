#BLACK JACK 

import random

suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
values = {"Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10, "Ace":11}
net_money = 100
playing = True 
number_of_games = 1


class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit, rank))
    
    def __str__(self):
        return self.deck 
    
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop(0)


class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self):
        self.cards.append(new_deck.deal())


def find_sum(cards):
    sum_of_hand = 0
    len_cards = len(cards)
    print(f"Number of cards in hand is {len_cards}")
    for i in range(len_cards):
        sum_of_hand += values[cards[i][1]]
    
    return sum_of_hand


def bust(sum_hand):
    player_bust = ""
    if(sum_hand > 21):
        player_bust = "Yes"
    
    return player_bust


def hit(cards):
    cards.append(new_deck.deal())
    return cards


def check_input(choice):
    choice = choice.capitalize()
    while True:
        if(choice == "Yes" or choice == "No"):
            break
        else:
            print("Sorry this is an invalid input!")
            choice = input("Enter Yes or No: ").capitalize()
    return choice 


while playing == True:
    print("--------------------------------")
    if number_of_games == 1:
        print("\nWelcome to Black Jack!")
    number_of_games += 1
    
    if net_money == 0 or net_money < 0:
        print("You have no money left!")
        print("Game over")
        print("Better luck next time!")
        break
    
    player_playing = input("Do you want to play?(Yes/No): ")
    player_playing = check_input(player_playing)
    if player_playing == "No":
        print(f"You have {net_money} cash left!")
        print("Okay, have a good day!")

        break
    
    print(f"\nYour net cash for round {number_of_games-1} is {net_money}")
    bet_in_range = False
    bet_is_int = False
    while bet_in_range == False or bet_is_int == False:
        player_bet = input(f"Enter your bet(between 0 and {net_money}): ")
        if player_bet.isdigit() == True:
            bet_is_int = True
            if int(player_bet) > net_money or int(player_bet) < 0:
                print(f"You don't have enough to bet {player_bet}")
                print("Try again!\n")
            else:
                bet_in_range = True
                break
        else:
            print("Invalid input, enter a number!")
        
    player_bet = int(player_bet)
    
    print("\nShuffling deck...")
    new_deck = Deck()
    new_deck.shuffle()
    
    print("Dealing you two cards")
    new_hand_player = Hand()
    new_hand_player.add_card()
    new_hand_player.add_card()
    print("Your hand is currently: ")
    for i in range(2):
        print(new_hand_player.cards[i][1] + " of " + new_hand_player.cards[i][0])
    sum_of_hand_player = find_sum(new_hand_player.cards)
    print(f"Your sum of hand is {sum_of_hand_player}\n")
    
    new_hand_comp = Hand()
    new_hand_comp.add_card()
    new_hand_comp.add_card()
    print("Computer has a " + new_hand_comp.cards[0][1] + " of " + new_hand_comp.cards[0][0])
    print("Other card in hand will not be revealed\n")
    
    hit_cards = input("Do you want a hit?(Yes/No):")
    hit_cards = check_input(hit_cards)
    
    while hit_cards == "Yes":
        new_hand_player.cards = hit(new_hand_player.cards)
        for i in range(len(new_hand_player.cards)):
            print(new_hand_player.cards[i][1] + " of " + new_hand_player.cards[i][0])
        sum_of_hand_player = find_sum(new_hand_player.cards)
        print(f"Your total sum is {sum_of_hand_player}")
        player_bust = bust(sum_of_hand_player)
        if player_bust == "Yes":
            print("You have been busted!")
            print(f"You lose your bet of {player_bet}")
            net_money -= player_bet
            break
        hit_cards = input("Do you want another hit?(Yes/No): ")
        hit_cards = check_input(hit_cards)
            
                    
    if(hit_cards == "No"):
        print("\n----------------------------------")
        print("\nComputer's turn to take hits!")
        sum_of_hand_computer = find_sum(new_hand_comp.cards)
        print(f"Computer's sum of hand is {sum_of_hand_computer}")
        while True:
            if sum_of_hand_computer > sum_of_hand_player:
                for i in range(len(new_hand_comp.cards)):
                    print(new_hand_comp.cards[i][1] + " of " + new_hand_comp.cards[i][0])
                print("Computer has higher sum than you do.\nSorry you lose your bet!")
                net_money -= player_bet
                break
            else:
                print("\nComputer is taking a hit")
                print("Computer's hand currently:")
                new_hand_comp.cards = hit(new_hand_comp.cards)
                for i in range(len(new_hand_comp.cards)):
                    print(new_hand_comp.cards[i][1] + " of " + new_hand_comp.cards[i][0])
                sum_of_hand_computer = find_sum(new_hand_comp.cards)
                print(f"Computer's sum of hand is now {sum_of_hand_computer}")
                computer_bust = bust(sum_of_hand_computer)
                if computer_bust == "Yes":
                    print("\nComputer has been busted!")
                    print("You have won this round!")
                    net_money += player_bet
                    break

