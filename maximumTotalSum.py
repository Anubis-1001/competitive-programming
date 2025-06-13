class Solution:
    def maximumTotalSum(self, maximumHeight: list[int]) -> int:
       maximumHeight.sort()
       total=0
       amnt=maximumHeight[len(maximumHeight)-1]
       for i in range(len(maximumHeight)-1, -1, -1):
           if amnt==0:
               return -1
           amnt=min(maximumHeight[i], amnt)
           total+=amnt
           amnt-=1
           
       return total

sol=Solution()

print(sol.maximumTotalSum([2,3,4,3]))
