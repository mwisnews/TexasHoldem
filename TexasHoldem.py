import itertools, random
from random import randint
import CreateDeck, ModifyDeck

deck = CreateDeck.createDeck()

card1 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck,card1)

card2 = ModifyDeck.newCard(deck)
ModifyDeck.removeCard(deck,card2)

print(card1.toString() + ' and ' + card2.toString())

if(card1.value == card2.value):
    print('Hey! Pocket ' + card1.value + 's!')

if(card1.color == card2.color):
    print('You have two ' + card1.color + '!')

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



