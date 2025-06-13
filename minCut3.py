import pprint

def minCut(s):

    dp=[[2001]*len(s) for _ in s]

    for end in range(0, len(dp)):
        for start in range(0, end+1):
            if end==start: dp[end][start] = 1
            if end-start >= 2: dp[end][start]=int(dp[end-1][start+1] == 1 and s[start] == s[end])
            else: dp[end][start]=int(s[start] == s[end])
            if dp[end][start] == 0: dp[end][start] = 2001

    #print(dp)


    return solve(0, len(s)-1, dp)-1

def solve(strt, end, dp):
    #print(strt, end)
    #if end < strt: return 0
    if dp[end][strt] != 2001: return dp[end][strt]

    minPalindrome=2001
    for i in range(strt, end):
        minPalindrome=min(minPalindrome, solve(strt, i, dp)+solve(i+1, end, dp))

    dp[end][strt] = minPalindrome
    return minPalindrome


pprint.pprint(minCut("abbba"))
pprint.pprint(minCut("beebe"))
pprint.pprint(minCut("abaccdeafaed"))
pprint.pprint(minCut("a"))
pprint.pprint(minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"))
