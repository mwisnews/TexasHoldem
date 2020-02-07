import itertools, random
from random import randint

# ModifyDeck will be a file to store helper functions that modify the deck in some way
# Examples include drawing a card from it or removing a card from it

def newCard(deck):
    return(deck[randint(0,len(deck)-1)])

def removeCard(deck, card):
    return deck.remove(card)

def burnCard(deck):
    burn = deck[randint(0, len(deck)-1)]
    return deck.remove(burn)