class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
      dp=[ [0]*(len(word2)+1) for _ in range(0, len(word1)+1) ]
      
      for i in range(0, len(dp)):
          for j in range(0, len(dp[0])):
              if j==0 or i==0:
                  dp[i][j]=max(i, j)
              else:
                  a=dp[i-1][j]+1
                  b=dp[i][j-1]+1
                  c=dp[i-1][j-1]
                  c+=1 if word1[i-1] != word2[j-1] else 0
                  dp[i][j] = min(a,b,c)

      return dp[len(word1)][len(word2)]


sol = Solution()
print(sol.minDistance("horse", "ros"))
print(sol.minDistance("intention", "execution"))
