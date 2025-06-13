def reachingPoints(sx, sy, tx, ty):
    while tx*ty > 0:
        print(sx, sy, tx, ty)
        if sy==ty and tx==sx:
            return True
        if ty > tx:
            ty= ty%tx
            if ty < sy and sy%tx == ty: ty = sy
        elif tx > ty:
            tx=tx%ty
            if tx < sx and sx%ty == tx: tx = sx

        else:
            return [sx, sy] == [tx, 0] or [sx, sy] == [0, ty] 

    return False


#print(reachingPoints(1, 8, 4, 15))
print(reachingPoints(9, 10, 9, 19))
