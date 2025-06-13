def findMinMoves(machines):
    s = sum(machines)
    n = len(machines)
    if s%n != 0:
        return -1
    t = s//n
    moves = 0
    dresses = 0
    prev_dresses = -1

    while prev_dresses != dresses:
        prev_dresses = dresses
        for i, m in enumerate(machines):
            dresses+= 1 if m > t else 0
            machines[i]-= 1 if m > t else 0
        moves+=1

    return moves-1


print(findMinMoves([0,0,11,5]))
