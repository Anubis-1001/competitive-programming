def is_n_straight_hand(hand, group_size):

    if len(hand) % group_size != 0:
        return False

    hand.sort()
    flag = True
    j = 0
    contador = 1

    for i in range(len(hand) - 1):

        flag = True
        if contador == group_size:
            contador = 1
            continue

        if hand[i] + 1 == hand[i + 1]:
            contador+=1
            continue

        j = i + 1
        while j < len(hand) and flag:
            if hand[i] + 1 == hand[j]:
                aux = hand[i+1]
                hand[i + 1] = hand[j]
                hand[j] = aux
                flag = False
                #print(i, "000", j)
            j += 1


        print(contador, " ---++ ", j)
        if j == len(hand) and contador % group_size != 0 :
            print(hand, "---")
            return False

        contador += 1

    print(hand, "---")
    return contador % group_size == 0



print(is_n_straight_hand([34,80,89,15,38,69,19,17,97,98,26,77,8,31,79,70,103,3,13,21,81,53,33,14,60,68,33,59,84,23,97,90,76,82,66,83,23,22,16,18,98,25,16,61,84,100,4,68,101,25,23,9,10,55,2,67,39,52,102,99,40,11,83,24,81,53,96,23,13,24,99,67,22,51,31,58,78,88,5,15,24,32,81,91,96,16,54,22,56,69,14,82,32,34,83,24,37,82,54,21], 4))
