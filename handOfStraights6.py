def isNStraightHand(hand, groupSize):
    hash_table = dict()

    for i in range(0, len(hand)):
        index = hand[i] % groupSize
        hash_index = hand[i]//groupSize 
        if hash_index not in hash_table:
            hash_table[hash_index] = [0]*groupSize
        hash_table.get(hash_index)[index]+=1


    print(hash_table.keys())
    control_sum = 0
    for key in hash_table:
        for i in hash_table.get(key):
            if hash_table.get(key)[i] == 0:
                if control_sum % groupSize != 0:
                    return False
    return True


print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
