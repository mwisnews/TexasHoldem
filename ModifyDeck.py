import itertools, random
from random import randint

def newCard(deck):
    return(deck[randint(0,len(deck)-1)])

def removeCard(deck, card):
    return deck.remove(card)