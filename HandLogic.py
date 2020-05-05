from collections import Counter
###
#  For the determine hand function, I thought it would be beneficial to represent a poker hand as an integer
#
#  Examples:       0 - High card at best (Remember to check for kicker)
#                  1 - One Pair (Remember to check for kicker)
#                  2 - Two Pair (Remember to check for kicker)
#                  3 - Three of a Kind (Remember to check for kicker)
#                  4 - Straight (Remember to check for high card)
#                  5 - Flush (Remember to check for high card)
#                  6 - Full House
#                  7 - Four of a Kind (Remember to check for kicker)
#                  8 - Straight Flush (Remember to check for high card)
#                  9 - Royal Flush
###

# Parameters: 
##          Input: Card array that holds both the cards in the player's hand as well as the cards in play
###
##          Output: Array that contains the determined hand strength (see example), the type of hand (ex straight, pair, etc)
#

def checkForStraight(values):
    hand = set(values)
    if 14 in hand:
        hand.add(1) ##Add alternative value for Ace
    #print(hand)
    for starter in (10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        needed_values = set(range(starter, starter+5))
        #print(needed_values)
        if(len(needed_values - hand) <= 0):
            return starter + 4

def determineHand(hand):
    handStrength = 0
    handType = ''
    bestHand = []
    values = []
    suits = []
    flush = False
    high_card = True

    for card in hand:
        values.append(card.value)
        suits.append(card.suit)
    
    value_hist = Counter(values)
    suits_hist = Counter(suits)
   
    print(value_hist)
    print(suits_hist)

    if checkForStraight(values) != None:
        handStrength = 4
        high_card = False

    if(handStrength == 0):
        handType = 'High Card'
    elif(handStrength == 1):
        handType = 'One Pair'
    elif(handStrength == 2):
        handType = 'Two Pair'
    elif(handStrength == 3):
        handType = 'Three of a Kind'
    elif(handStrength == 4):
        if(checkForStraight(values) == 11):
            handType = 'Jack high straight'
        elif(checkForStraight(values) == 12):
            handType = 'Queen high straight' 
        elif(checkForStraight(values) == 13):
            handType = 'King high straight'
        elif(checkForStraight(values) == 14):
            handType = 'Ace high straight'  
        else: 
            handType = str(checkForStraight(values)) + ' high straight'
    elif(handStrength == 5):
        handType = 'Flush'
    elif(handStrength == 6):
        handType = 'Full House'
    elif(handStrength == 7):
        handType = 'Four of a Kind'
    elif(handStrength == 8):
        handType = 'Straight Flush'
    elif(handStrength == 9):
        handType = 'Royal Flush'
    else:
        handType = 'Error'

    result = [handStrength, handType, bestHand]
    return result