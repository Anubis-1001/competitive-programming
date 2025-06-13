def isNStraightHand(hand, groupSize):

    hand.sort()
    arr_size = 0
    i = 0
    while i < len( hand ):
        if arr_size == 0:
            i = 0
            last = hand[i]-1
        if ( last + 1 == hand[i]):
            last = hand[i]
            hand.pop(i)
            arr_size = ( arr_size + 1 ) % groupSize
        else:
            i+=1
    
    return len(hand) == 0 and arr_size == 0 
    
print(isNStraightHand([1,2,3,4,5], 4))
