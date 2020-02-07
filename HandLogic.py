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
##          Output: Array that contains both the determined hand strength (see example) as well as the best 
#                   5 card hand they can make

def determineHand(hand):
    handStrength = 0
    bestHand = []


    result = [handStrength, bestHand]
    return result