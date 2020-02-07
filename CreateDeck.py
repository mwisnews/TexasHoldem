import itertools, random
import time
from random import randint

# CreateDeck contains the definition of a Card object as well as the function that creates a shuffled deck

class Card:
    def __init__(self,value,color):
        self.value = value
        self.color = color
    def toString(self):
        return self.value + " of " + self.color

def createDeck():
    colors = ['hearts', 'diamonds', 'spades', 'clubs']
    values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    deck = [Card(value,color) for value in values for color in colors]
    random.shuffle(deck)
    time.sleep(random.random())
    random.shuffle(deck)
    time.sleep(random.random())
    random.shuffle(deck)
    return deck