import itertools, random
from random import randint
import CreateDeck, ModifyDeck, DealHand, ClearScreen

cardsInPlay = []

deck = CreateDeck.createDeck()
hand = DealHand.dealHand(deck)

#Initial hand is dealt, at this point player is in

cardsInHand = ('The cards in your hand are ' + hand[0].toString() + ' and ' + hand[1].toString())

#First burn card
ModifyDeck.burnCard(deck)

#Flop first card
flop1 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop1)
cardsInPlay.append(flop1)

#Flop second card
flop2 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop2)
cardsInPlay.append(flop2)

#Flop third card
flop3 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop3)
cardsInPlay.append(flop3)

playStatus = 'The cards in play are: ' + flop1.toString() + ', ' + flop2.toString() + ', ' + flop3.toString()

print(cardsInHand)
print(playStatus)
input()

#Second burn card
ModifyDeck.burnCard(deck)

#Turn
turn = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, turn)
cardsInPlay.append(turn)

playStatus += ', ' + turn.toString()

ClearScreen.clear()
print(cardsInHand)
print(playStatus)
input()

#Third burn card
ModifyDeck.burnCard(deck)

#River
river = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, river)
cardsInPlay.append(river)

playStatus += ', ' + river.toString()

ClearScreen.clear()
print(cardsInHand)
print(playStatus)
input()

#Determine who wins




