# About program
# In this project, a main program and some functions are given, but you need to 
# implement three classes used by the main program: Card(), Deck(), and PlayingHand(). 
# Each card has two primary attributes: rank and suit. In a deck, 
# there are four suits -- hearts, spades, diamonds, and clubs --, 
# that we represent by their first letters: H(h), S(s), D(d), C(c). 
# Each suit has thirteen cards -- Ace, 2-10, Jack, Queen, and King – with ranks 1-13 in that order. 
# Thus, a deck has 52 cards. A playing hand has thirteen cards.
import random

class Card():
    def __init__(self, rank = "", suit = ""):
        rank_dict = {"1":"A","11":"J","12":"Q","13":"K"}
        #if(type(rank) == str):
        #    if rank in '111213':
        #        rank = int(rank)
        #        #pass

        if(type(rank) == int):
            if rank >= 1 and rank <= 13:
                if rank >= 2 and rank <= 10:
                    rank = str(rank)
                elif str(rank) in rank_dict:
                    rank = str(rank)
                    rank = rank_dict[rank]

        if rank not in '12345678910111213aAjJqQkK':
            rank = "blk"

        if type(suit) == int or suit not in "SDHCsdhc":
            suit = "blk"
        
        #if self.is_blank() == False:
        if rank == "" or suit == "":
            rank = "blk"
            suit = "blk"

        self.suit = suit
        self.rank = rank

    def __str__(self):
        if self.rank != "blk" and self.suit != "blk" or self.is_blank() == False:
            return "{:>3}{}".format(self.rank.upper(),self.suit.upper())
        else:
            return "{}".format("blk")

    def is_blank(self):
        if self.rank == "" or self.suit == "":
            return False
        else:
            return True

class Deck():
    def __init__(self):
        deck = []
        suits = "hsdc"
        for suit in suits:    
            for card in range(1,14):
                card_name = str(Card(str(card),suit)).strip()
                deck.append(card_name)
        self.deck = deck
        # A constructor without any parameters. The constructor creates a deck of 52 cards.
    
    def __str__(self):
        printed = ""
        #print(self.deck)
        deck_of_thirteen = [self.deck[x:x+13] for x in range(0, len(self.deck), 13)]
        for thirteen in deck_of_thirteen:
            printed += (" {:>3}"*len(thirteen)).format(*thirteen) + "\n"
        return printed
        # Method __str__() for returning a string representation of a deck, consisting of 4 lines containing 13 cards each.
    
    def shuffle(self):
        random.shuffle(self.deck)

        # Method shuffle(). Shuffles the cards in the deck.
    
    def deal(self):
        hand1 = []
        hand2 = []
        hand3 = []
        hand4 = []

        while len(self.deck) > 0:
            hand1.append(self.deck.pop())
            hand2.append(self.deck.pop())
            hand3.append(self.deck.pop())
            hand4.append(self.deck.pop())

        return hand1, hand2, hand3, hand4

class PlayingHand():
    # A constant, NUMBER_CARDS, with value 13
    NUMBER_CARDS = 13

    def __init__(self):
        self.blank_cards = 13
        # A constructor without any parameters. The constructor creates a hand of 13 blank cards.
    
    def __str__(self):
        return "string representation of a playing hand, consisting of a single line containing a string representation of each card"
        # Method __str__() for returning a string representation of a playing hand, consisting of a single line containing a string representation of each card.
    
    def add_card(self):
        pass
        # Method add_card() with the parameter denoting a card. The methods adds the given card to the playing hand at the first blank position.

# Main program and functions given:
def test_cards():
    card1 = Card()
    print(card1)
    card2 = Card(5,'s')
    print(card2)
    card3 = Card('Q','D')
    print(card3)
    card4 = Card('x', 7)
    print(card4)

def print_4_hands(hand1, hand2, hand3, hand4):
    ''' Prints the 4 hands '''
    print(hand1)
    print(hand2)
    print(hand3)
    print(hand4)

def deal_4_hands(deck, hand1, hand2, hand3, hand4):
    ''' Deals cards for 4 hands '''
    for i in range(PlayingHand.NUMBER_CARDS):
        hand1.add_card(deck.deal())
        hand2.add_card(deck.deal())
        hand3.add_card(deck.deal())
        hand4.add_card(deck.deal())

def test_hands(deck):
    hand1 = PlayingHand()
    hand2 = PlayingHand()
    hand3 = PlayingHand()
    hand4 = PlayingHand()
    print("The 4 hands:")
    print_4_hands(hand1, hand2, hand3, hand4)
    deal_4_hands(deck, hand1, hand2, hand3, hand4)
    print("The 4 hands after dealing:")
    print_4_hands(hand1, hand2, hand3, hand4)

# The main program starts here
random.seed(10)
test_cards()
deck = Deck()
deck.shuffle()
print("The deck:")
print(deck)
test_hands(deck)
print("The deck after dealing:")
print(deck)

# blk
#  5S
#  QD
# blk
# The deck:
#  6D 10H JS QC JD 5S AH 9S AC 5D 7H QD 2D
#  8S 9D 2C 10D QS KS 7S 2H 4D 3S 6H 3H QH
#  4S 3C 5C 9C KH 7D 10C 6C 4C 2S 6S JC 9H
#  KD 3D JH 5H 8C 8H 4H AS KC 8D 7C AD 10S
# The 4 hands:
#  blk blk blk blk blk blk blk blk blk blk blk blk blk
#  blk blk blk blk blk blk blk blk blk blk blk blk blk
#  blk blk blk blk blk blk blk blk blk blk blk blk blk
#  blk blk blk blk blk blk blk blk blk blk blk blk blk
# The 4 hands after dealing:
#  6D JD AC 2D 10D 2H 3H 5C 10C 6S 3D 8H 8D
# 10H 5S 5D 8S QS 4D QH 9C 6C JC JH 4H 7C
#  JS AH 7H 9D KS 3S 4S KH 4C 9H 5H AS AD
#  QC 9S QD 2C 7S 6H 3C 7D 2S KD 8C KC 10S
# The deck after dealing: