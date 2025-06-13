class Solution:
  def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
    while tx*ty > 0:
        print(sx, sy, tx, ty) 
        if ( tx%ty == sx%sy and sy==ty and tx >= sx ) or ( ty%tx == sy%sx and tx==sx and ty >= sy ):
            return True
        if ty > tx: 
            ty= ty%tx
        elif tx > ty: 
            tx=tx%ty
        else:
            return [sx, sy] == [tx, 0] or [sx, sy] == [0, ty] 

    return False

