import bisect

def swimInWater(grid):
    accesed=dict({0: [0,0]})
    available=[0]
    maximun=0
    last=grid[len(grid)-1][len(grid[0])-1]
    while len(available) > 0:
        current=available.pop(0)
        maximun=max(maximun, current)
        if current == last:
            return maximun
        y=accesed[current][0]
        x=accesed[current][1]
        for idx,idy in [(1,0), (-1,0), (0,-1), (0,1)]:
            ny=idy+y
            nx=idx+x
            ny=min(max(0, ny),len(grid)-1)
            nx=min(max(0, nx),len(grid)-1)
            element=grid[ny][nx]
            if element not in accesed:
                accesed[element] = [ny, nx]
                available.insert(bisect.bisect_left(available, element), element)

    return -1


print(swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
