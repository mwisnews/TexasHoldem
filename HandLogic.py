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
#                   as well as the best 5 card hand they can make

def determineHand(hand):
    handStrength = 0
    handType = ''
    bestHand = []



    if(handStrength == 0):
        handType = 'High Card'
    elif(handStrength == 1):
        handType = 'One Pair'
    elif(handStrength == 2):
        handType = 'Two Pair'
    elif(handStrength == 3):
        handType = 'Three of a Kind'
    elif(handStrength == 4):
        handType = 'Straight'
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