import itertools, random
from random import randint
import CreateDeck, ModifyDeck, DealHand

deck = CreateDeck.createDeck()
hand = DealHand.dealHand(deck)

print(hand[0].toString() + ' and ' + hand[1].toString())

if(hand[0].value == hand[1].value):
    print('Hey! Pocket ' + hand[1].value + 's!')

if(hand[0].color == hand[1].color):
    print('You have two ' + hand[1].color + '!')

facedown1 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, facedown1)

flop1 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop1)

flop2 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop2)

flop3 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, flop3)

flopResult = 'The cards in play are: ' + flop1.toString() + ', ' + flop2.toString() + ', ' + flop3.toString()

print(flopResult)

facedown2 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, facedown2)

turn = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, turn)

turnResult = flopResult + ', ' + turn.toString()
print(turnResult)

facedown3 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, facedown3)

river = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck, river)

riverResult = turnResult + ', ' + river.toString()
print(riverResult)



