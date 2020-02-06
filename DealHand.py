import ModifyDeck

def dealHand(deck):
    card1 = ModifyDeck.newCard(deck)
    ModifyDeck.removeCard(deck,card1)
    card2 = ModifyDeck.newCard(deck)
    ModifyDeck.removeCard(deck,card2)
    return [card1, card2]