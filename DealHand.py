import ModifyDeck,CreateDeck

#DealHand is called in the beginning of the game when cards are being dealt to players

def dealHand(deck):
    card1 = ModifyDeck.newCard(deck)
    ModifyDeck.removeCard(deck,card1)
    #card1 = CreateDeck.Card(14,'Ace', 'hearts')
    card2 = ModifyDeck.newCard(deck)
    ModifyDeck.removeCard(deck,card2)
    #card2 = CreateDeck.Card(4,'4', 'diamonds')
    return [card1, card2]
