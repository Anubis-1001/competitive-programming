class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
       if len(points) == 1:
        return 1
       lines = dict()
       start = 1
       maxLines = 0
       for point1 in points:
           print(point1)
           lines = dict()
           for point2 in points[start:]:
               if ( point2[0] != point1[0] ):
                   m = (point2[1]-point1[1])/(point2[0]-point1[0])+0
                   b = point1[1]-m*point1[0]
                   mykey = f"{m}:{b}"
               else:
                   mykey=f":{point1[0]}"

               if  mykey not in lines:
                   lines[mykey] = 1

               lines[mykey]+=1
               maxLines = max(lines[mykey], maxLines)
               print(mykey)
               print(maxLines)
           del lines
           start+=1

       return maxLines

