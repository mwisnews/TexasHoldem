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
    flush_suit = ''
    high_card = True

    for card in hand:
        values.append(card.value)
        suits.append(card.suit)
    
    #Counters for Pairs and Flush Data
    value_hist = Counter(values)
    suits_hist = Counter(suits)
   
    ##Variables for Pairs and Flush
    pairs = []
    triple = []
    quadruple = []
    flush_values = []

    for key, value in value_hist.items():
        if(value == 1):
            pass
        elif(value == 2):
            high_card = False
            pairs.append(key)
        elif(value == 3):
            high_card = False
            triple.append(key)
        elif(value == 4):
            high_card = False
            quadruple.append(key)
        else:
            print("Error in searching for pairs")
    
    #If there is a single pair
    if len(pairs) == 1 and len(triple) == 0 and len(quadruple) == 0:
        handStrength = 1
    
    #If there are multiple pairs
    if len(pairs) > 1 and len(triple) == 0 and len(quadruple) == 0:
        handStrength = 2
        if len(pairs) > 2:
            if pairs[0] < pairs[1] and pairs[0] < pairs[2]:
                pairs.remove(pairs[0])
            elif pairs[1] < pairs[0] and pairs[1] < pairs[2]:
                pairs.remove(pairs[1])
            elif pairs[2] < pairs[1] and pairs[2] < pairs[0]:
                pairs.remove(pairs[2])
            else:
                print("Error removing extra pair")

    #If there are three of a kind
    if len(pairs) == 0 and len(triple) == 1 and len(quadruple) == 0:
        handStrength = 3   

    #Check for Straight
    if checkForStraight(values) != None:
        handStrength = 4
        high_card = False


    #Check for Flush
    for key, value in suits_hist.items():
        if value > 4:
            flush_suit = key
            handStrength = 5
    #Get values of Flush Cards
    if flush_suit != '':
        for card in hand:
            if card.suit == flush_suit:
                flush_values.append(card.value)
        flush_values.sort()
    
    #Check for Full House
    #Exactly 1 pair and 1 triple
    if len(pairs) == 1 and len(triple) == 1 and len(quadruple) == 0:
        handStrength = 6
    #1 triple and 2 pairs
    elif len(pairs) == 2 and len(triple) == 1 and len(quadruple) == 0:
        handStrength = 6
        if(pairs[0] < pairs[1]):
            pairs.remove(pairs[0])
        else:
            pairs.remove(pairs[1])
    #2 triples
    elif len(pairs) == 0 and len(triple) == 2 and len(quadruple) == 0:
        handStrength = 6
        if(triple[0] < triple[1]):
            pairs.append(triple[0])
            triple.remove(triple[0])
        else:
            pairs.append(triple[1])
            triple.remove(triple[1])


    if(handStrength == 0):
        handType = 'High Card'

    elif(handStrength == 1):
        if pairs[0] <= 10 and pairs[0] >1:
            handType = 'Pair of ' + str(pairs[0]) + 's'
        elif pairs[0] == 11:
            handType = 'Pair of Jacks'
        elif pairs[0] == 12:
            handType = 'Pair of Queens'
        elif pairs[0] == 13:
            handType = 'Pair of Kings'
        elif pairs[0] == 14:
            handType = 'Pair of Aces'
        else:
            print('Error in printing what pair is')

    elif(handStrength == 2):
        pair1_name = pairs[0]
        pair2_name = pairs[1]

        if pair1_name == 11:
            pair1_name = 'Jack'
        elif pair1_name == 12:
            pair1_name = 'Queen'
        elif pair1_name == 13:
            pair1_name = 'King'
        elif pair1_name == 14:
            pair1_name = 'Ace'
        else:
            pass
        
        if pair2_name == 11:
            pair2_name = 'Jack'
        elif pair2_name == 12:
            pair2_name = 'Queen'
        elif pair2_name == 13:
            pair2_name = 'King'
        elif pair2_name == 14:
            pair2_name = 'Ace'
        else:
            pass
        handType = 'Two Pair: ' + str(pair1_name) + 's and ' + str(pair2_name) + 's'

    elif(handStrength == 3):
        if triple[0] <= 10 and triple[0] >1:
            handType = 'Three ' + str(triple[0]) + 's'
        elif triple[0] == 11:
            handType = 'Three Jacks'
        elif triple[0] == 12:
            handType = 'Three Queens'
        elif triple[0] == 13:
            handType = 'Three Kings'
        elif triple[0] == 14:
            handType = 'Three Aces'
        else:
            print('Error in printing what pair is')

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
        if(flush_values[-1] > 1 and flush_values[-1] <= 10):
            handType = str(flush_values[-1]) + ' high ' + str(flush_suit) + ' Flush'
        elif(flush_values[-1] == 11):
            handType = 'Jack high ' + str(flush_suit) + ' Flush'
        elif(flush_values[-1] == 12):
            handType = 'Queen high ' + str(flush_suit) + ' Flush'
        elif(flush_values[-1] == 13):
            handType = 'King high ' + str(flush_suit) + ' Flush'
        elif(flush_values[-1] == 14):
            handType = 'Ace high ' + str(flush_suit) + ' Flush'
        else:
            print('Error determining flush high card')

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