import itertools, random
import time
from random import randint

# CreateDeck contains the definition of a Card object as well as the function that creates a shuffled deck

class Card:
    def __init__(self,value, name, suit):
        self.value = value
        self.suit = suit
        self.name = name

    def toString(self):
        return self.name + " of " + self.suit

def createDeck():
    suits = ['hearts', 'diamonds', 'spades', 'clubs']
    values = {'Ace':14, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':11, 'Queen':12, 'King':13}
    deck = [Card(values[name],name,suit) for name in values for suit in suits]
    random.shuffle(deck)
    time.sleep(random.random())
    random.shuffle(deck)
    time.sleep(random.random())
    random.shuffle(deck)
    return deck