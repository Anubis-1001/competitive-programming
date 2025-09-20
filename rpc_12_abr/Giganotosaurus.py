t = int(input())
p = input()
j = len(p)
p = p+"."*(t*t-len(p))
#         jump             pos
dp = [ [0]*3*t for _ in range(3*t) ]
dp[0][0]=1

MOD=10**9+7

for i in range(j):
    if p[i] == "#":
        continue
    for x in range(t):
        if x < len(dp[0]) i+1 < 3*t and i+1 < len(p) and p[i+1] == ".":
            dp[i+1][x]+=dp[i][x]
            dp[i+1][x]%=MOD
        if x+1 < len(dp[0]) and i+x+2 < 3*t  and i+x+2 < len(p) and p[i+x+2] == ".":
            dp[i+x+2][x+1]+=dp[i][x]
            dp[i+x+2][x+1]%=MOD

suma=0

#print(dp)
for i in range(t, len(dp[0])):
    suma+=sum(dp[i])
    suma%=MOD

print(suma % MOD )
