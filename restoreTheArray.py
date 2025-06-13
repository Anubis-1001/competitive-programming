def numberOfArrays(s, k):
    dp = [0]*(len(s)+1)
    dp[0] = 1
    for i in range(1, len(s)+1):
        if s[i-1] == "0":
            ind = i-1
            num = ""
            while ind >= 0 and s[ind] == "0":
                num = s[ind]+num
                ind-=1
            num = s[ind]+num
            if int(num) > k:
                return 0
            continue
        for j in range(i-1, -1, -1):
            n = int(s[j:i])
            #print(n)
            if n <= k:
                dp[i]+=dp[j]
    print(dp)
    return dp[-1]

print(numberOfArrays("1317", 2000))
print(numberOfArrays("1000", 1000))
print(numberOfArrays("1000", 10))
print(numberOfArrays("1234567890", 90))

