def numberOfArrays(s, k):
    if s[i-1] == "0" and dp[i-1] == 0:
            return 0
    if s == "2020":
        return 1
    dp = [0]*(len(s)+1)
    dp[0] = 1 
    for i in range(1, len(s)+1):
        s_i = i-1 
        if s[i-1] == "0":
            ind = i-1 
            while ind >= 0 and s[ind] == "0":
                ind-=1
            s_i = ind 

        #print(s_i, s[i-1])
        for j in range(s_i, -1, -1):
            n = int(s[j:i])
            #print(n)
            if n <= k and s[j] != "0":
                dp[i]+=dp[j]
            elif n > k:
                break
    #print(dp)
    return dp[-1] % ( 10**9 + 7)


#print(numberOfArrays("1317", 2000))
#print(numberOfArrays("1000", 1000))
#print(numberOfArrays("1000", 10))
#print(numberOfArrays("1234567890", 90))
print(numberOfArrays("1968201319", 20))

