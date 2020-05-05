import itertools, random
from random import randint
import CreateDeck, ModifyDeck, DealHand, ClearScreen, HandLogic

cardsInPlay = []
totalCards = []

deck = CreateDeck.createDeck()
hand = DealHand.dealHand(deck)

for i in hand:
    totalCards.append(i)

#Initial hand is dealt, at this point player is in

cardsInHand = ('The cards in your hand are ' + hand[0].toString() + ' and ' + hand[1].toString())

#First burn card
ModifyDeck.burnCard(deck)

#Flop first card
flop1 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop1)
#flop1 = CreateDeck.Card(9,'9', "diamonds")
cardsInPlay.append(flop1)
totalCards.append(flop1)

#Flop second card
flop2 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop2)
#flop2 = CreateDeck.Card(13, 'King', 'diamonds')
cardsInPlay.append(flop2)
totalCards.append(flop2)

#Flop third card
flop3 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop3)
#flop3 = CreateDeck.Card(12, 'Queen', 'diamonds')
cardsInPlay.append(flop3)
totalCards.append(flop3)

playStatus = 'The cards in play are: ' + flop1.toString() + ', ' + flop2.toString() + ', ' + flop3.toString()

print(cardsInHand)
print(playStatus)
input()

#Second burn card
ModifyDeck.burnCard(deck)

#Turn
turn = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, turn)
#turn = CreateDeck.Card(6, '6', 'diamonds')
cardsInPlay.append(turn)
totalCards.append(turn)

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
#river = CreateDeck.Card(11, 'Jack', 'diamonds')
cardsInPlay.append(river)
totalCards.append(river)

playStatus += ', ' + river.toString()

ClearScreen.clear()
print(cardsInHand)
print(playStatus)
#input()


#Determine what the player has
yourHand = HandLogic.determineHand(totalCards)

print(yourHand)