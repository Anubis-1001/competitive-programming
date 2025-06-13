def isNStraightHand(hand, groupSize):

    hand.sort()
    i = 0
    while i < len( hand ) - 1:
        if  i % groupSize == 0 or hand[i] + 1 == hand[i+1] or hand[i] == hand[i+1] - i % groupSize :
            i+=1
        else:
            hand.append( hand.pop(i) )

        #elif hand[i] < hand[i-1] and hand[i] < hand[i+1]:
         #   break
    print('hand is ',hand)
    return i % groupSize == 0
     
    
print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
