""" 
Author: Akshat Bhat
Description: A OOP-based Python program for the classic blackjac game
"""

import random
# Global Variables
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11} 
# Later Ace will be made 1 if needed but always first consider Ace value to be 11
playing = True
total = None

print("WELCOME TO BLACKJACK - GAME BETWEEN COMPUTER DEALER AND HUMAN PLAYER\n")

while True:
    try:
        total = int(input("Enter initial amount of chips you have: "))  
    except:
        print('We take only Integer Value. Please provide an integer.\n')
    else:
        break

class Card():
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return "{} of {}".format(self.rank,self.suit)
        
class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                (self.deck).append(card)
    
    def __str__(self):
        returnstring = ''
        for card in self.deck:
            returnstring += '\n' + card.__str__()
        return "The deck has:- " + returnstring

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = (self.deck).pop()
        return single_card

class Hand(): # Basically a representation of a player 
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        (self.cards).append(card)
        self.value += values[card.rank]
        
        #track Aces
        if card.rank is 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        # if total value is more than 21 and I still have an Ace then change the Ace value to one instead of eleven which was initial Ace value
        # so reduce the total value by 10 and no. of Aces by 1 (as now Ace value is 1)
        while self.value>21 and self.aces!=0:
            self.value -= 10
            self.aces -= 1

class Chips():
    
    def __init__(self):
        self.bet = 0
        
    def win_bet(self):
        global total
        total += self.bet
    
    def lose_bet(self):
        global total
        total -= self.bet

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except:
            print('We take only Integer Value. Please provide an integer.\n')
        else:
            if chips.bet>total:
                print('Insufficient Chips! You have {} chips only!\n'.format(total))
            else:
                print('Your bet was {}!\n'.format(chips.bet))
                break
            
def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(deck,hand):
    global playing  # to control an game running while loop
    while True:
        print("Hit(h) or Stand(s)?")
        c = input("Your Choice: ")
        if c == 'h':
            hit(deck,hand)
            if hand.value>21:
                break
            show_some(playerhand,dealerhand)    
        elif c =='s':
            print("Player Stands! Dealer's turn...\n")
            playing = False
            break
        else:
            print('Wrong input! Enter again...\n')

def show_some(player,dealer):
    playerhand = ''
    dealerhand = ''
    for card in player.cards:
        playerhand += '\n' + card.__str__()
    print("PLAYER HAND:- " + playerhand +"\n")
    for card in dealer.cards[1:]:
        dealerhand += '\n' + card.__str__()
    print("DEALER HAND(Top card hidden so not shown):- " + dealerhand +"\n")
    
def show_all(player,dealer):
    playerhand = ''
    dealerhand = ''
    for card in player.cards:
        playerhand += '\n' + card.__str__()
    print("PLAYER HAND:- " + playerhand +"\n")
    for card in dealer.cards:
        dealerhand += '\n' + card.__str__()
    print("DEALER HAND(All shown):- " + dealerhand +"\n")
    
def player_busts(chips):
    print("PLAYER BUST!\n")
    chips.lose_bet()

def player_wins(chips):
    print("PLAYER WINS!\n")
    chips.win_bet()

def dealer_busts(chips):
    print("DEALER BUST!\n")
    print("PLAYER WINS!\n")
    chips.win_bet()
    
def dealer_wins(chips):
    print("DEALER WINS!\n")
    chips.lose_bet()
    
def push():
    print('Dealer and Player Tie! PUSH!!\n')


while True:    
    print("\nSTARTING A NEW GAME...\n")
    deck = Deck()
    deck.shuffle()
    print("Deck Shuffled...\n")
    
    playerhand = Hand()
    playerhand.add_card(deck.deal())
    playerhand.add_card(deck.deal())
    print("Two cards dealt to Player...\n")
    
    dealerhand = Hand()
    dealerhand.add_card(deck.deal())
    dealerhand.add_card(deck.deal())
    print("Two cards dealt to Dealer...\n")
    
    playerchips = Chips()
    take_bet(playerchips)
    
    show_some(playerhand,dealerhand)
    
    if playerhand.value==21:
        print("PLAYER WINS ON ACCOUNT OF BLACKJACK!!!")
        player_wins(playerchips)
        playing = False
        
    while playing:  # recall this variable from our hit_or_stand function
        
        hit_or_stand(deck,playerhand)
        show_some(playerhand,dealerhand)

        if playerhand.value>21:
            player_busts(playerchips)
            break
        else:
            while dealerhand.value<=17:
                print("Dealer Hits...\n")
                hit(deck,dealerhand)
                show_all(playerhand,dealerhand)
            print("FINAL HANDS:- ")
            show_all(playerhand,dealerhand)
            if dealerhand.value>21:
                dealer_busts(playerchips)
            elif playerhand.value<dealerhand.value:
                dealer_wins(playerchips)
            elif playerhand.value>dealerhand.value:
                player_wins(playerchips)
            elif playerhand.value==dealerhand.value:
                push()
            
    print("\nPlayer Total Chips = {}".format(total))
    
    if total==0:
        print("\nYou have lost all your chips!!")
        print("Thank you for playing Blackjack!\n")
        break
    
    choice = input("Would you like to play another hand? (y/n)\n")
    if choice[0].lower()=='y':
        playing = True
        print("\n"*100)
        continue
    elif choice[0].lower()=='n':
        print("\nThank you for playing Blackjack!\nYou are going home with {} chips!\n".format(total))
        break