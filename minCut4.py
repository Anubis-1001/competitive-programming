import pprint

def minCut(s):

    dp=[[2001]*len(s) for _ in s]
    return solve(0, len(s)-1, dp, s)-1

def solve(strt, end, dp, s):
    #print(strt, end)
    if end == strt:
        dp[end][strt]=1
        return 1
    if end-strt >= 2: dp[end][strt]=int(dp[end-1][strt+1] == 1 and s[strt] == s[end])
    else: dp[end][strt]=int(s[strt] == s[end])
    if dp[end][strt] == 0: dp[end][strt]=2001
    if dp[end][strt] != 2001: return dp[end][strt]

    minPalindrome=2001
    for i in range(strt, end):
        minPalindrome=min(minPalindrome, solve(strt, i, dp, s)+solve(i+1, end, dp, s))

    dp[end][strt] = minPalindrome
    return minPalindrome


pprint.pprint(minCut("abbba"))
pprint.pprint(minCut("beebe"))
pprint.pprint(minCut("abaccdeafaed"))
pprint.pprint(minCut("a"))
#pprint.pprint(minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"))
