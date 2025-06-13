def isNStraightHand(hand, groupSize):

    hand.sort()
    i = 0
    while i < len( hand ) - 1:
        if ( i % groupSize == 0 and i > 0 and hand[-1] < hand[i] ) or hand[i] == hand[i+1]:
            hand.append( hand.pop(i) )
        elif hand[i] + 1 == hand[i+1] or ( i + 1 ) % groupSize == 0:
            i+=1
    return i == len(hand)-1 and ( i + 1 ) % groupSize == 0
     
    
print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(isNStraightHand([1,2,3,4,5], 4), "000`")
print(isNStraightHand([8, 10, 12], 3))

