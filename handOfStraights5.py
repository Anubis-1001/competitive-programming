def isNStraightHand(hand, groupSize):

    if( len(hand) % groupSize != 0):
        return False

    count_arr = [0]*groupSize

    for i in range(0, len(hand)):
        index = hand[i] % groupSize
        count_arr[index] += 1
        if count_arr[index] > groupSize:
            return False

    return True


print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
