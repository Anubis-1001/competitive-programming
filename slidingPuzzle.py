from copy import deepcopy 

def slidingPuzzle(board):
    board=[[str(board[0][0]),str( board[0][1]),str( board[0][2]),str( board[1][0]),str( board[1][1]),str( board[1][2])], 0]
    queue=[board]
    scanned={}
    while queue:
        print(queue)
        state=queue.pop(0)
        if state[0] == ["1","2","3","4","5","0"]:
            return state[1]
        z_idx=state[0].index("0")
        if z_idx%3 < 2:
            next_state=deepcopy(state)
            next_state[0][z_idx], next_state[0][z_idx+1] = next_state[0][z_idx+1], next_state[0][z_idx]
            next_state[1]+=1
            str_repr="".join(next_state[0])
            if str_repr not in scanned:
                scanned[str_repr] = True
                queue.append(next_state)
            print(next_state, "====")

        if z_idx%3 > 0:
            next_state=deepcopy(state)
            next_state[0][z_idx], next_state[0][z_idx-1] = next_state[0][z_idx-1], next_state[0][z_idx]
            next_state[1]+=1
            str_repr="".join(next_state[0])
            if str_repr not in scanned:
                scanned[str_repr] = True
                queue.append(next_state)
            print(next_state, "====")

        next_state=deepcopy(state)
        next_state[0][z_idx], next_state[0][(z_idx+3)%6] = next_state[0][(z_idx+3)%6], next_state[0][z_idx]
        next_state[1]+=1
        str_repr="".join(next_state[0])
        if str_repr not in scanned:
            scanned[str_repr] = True
            queue.append(next_state)

        print(next_state, "====")



    return -1


print(slidingPuzzle([[4,1,2],[5,0,3]]))
