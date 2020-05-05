import ModifyDeck,CreateDeck

#DealHand is called in the beginning of the game when cards are being dealt to players

def dealHand(deck):
    card1 = ModifyDeck.newCard(deck)
    ModifyDeck.removeCard(deck,card1)
    #card1 = CreateDeck.Card(9,'9', 'diamonds')
    card2 = ModifyDeck.newCard(deck)
    ModifyDeck.removeCard(deck,card2)
    return [card1, card2]
