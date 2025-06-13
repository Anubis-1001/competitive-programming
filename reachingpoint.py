def reachingPoints(sx, sy, tx, ty):
    while tx*ty > 0:
        print(sx, sy, tx, ty)
        if ( tx%ty == sx%sy and sy==ty) or ( ty%tx == sy%sx and tx==sx):
            return True
        if ty > tx:
            ty= ty%tx
        elif tx > ty:
            tx=tx%ty
        else:
            return [sx, sy] == [tx, 0] or [sx, sy] == [0, ty] 

    return False


print(reachingPoints(1, 8, 4, 15))
