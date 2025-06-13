def isNStraightHand(hand, groupSize):

    if ( len(hand) == 0):
        return True
    hand.sort()
    arr_size = 0
    last = hand[0]-1
    next_iteration = []
    for i in range(0, len(hand)):
        if ( last + 1 == hand[i]):
            last = hand[i]
            arr_size = ( arr_size + 1 ) % groupSize
            if arr_size == 0:
                return isNStraightHand(next_iteration + hand[i+1:], groupSize)
        elif last == hand[i]:
            next_iteration.append(hand[i])
        else:
            return False
    
    return False
    
    


print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
