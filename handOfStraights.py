def isNStraightHand(hand, groupSize):

    hand.sort()
    arr_size = 0
    last = hand[0]-1
    i = 0
    while arr_size != 0 or i < len(hand):
        if ( last + 1 == hand[i]):
            last = hand[i]
            hand.pop(i)
            arr_size = ( arr_size + 1 ) % groupSize
        else:
            i+=1
            if( i >= len(hand) ):
                return False
    if ( groupSize != 0 ):
        return False
    return True


print(isNStraightHand([1,2,3,6,2,3,4,7,8], 2))
