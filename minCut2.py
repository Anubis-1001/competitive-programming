import pprint

def minCut(s):
    dpPalindrome=[[False]*len(s) for _ in s]
    dp=[[2001]*len(s) for _ in s]
    for x in range(0, len(s)):
        dp[x][x]=1

    return solve(0, len(s)-1, dp, s)-1

def solve(strt, end, dp, s):
    #print(strt, end)
    #if end < strt: return 0
    if dp[end][strt] != 2001: return dp[end][strt]
    if s[strt] == s[end] and ( dp[end-1][strt+1] == 1 or end-strt == 1): 
        dp[strt][end]=1
        return 1

    minPalindrome=2001
    for i in range(strt, end):
        minPalindrome=min(minPalindrome, solve(strt, i, dp, s)+solve(i+1, end, dp, s))

    dp[end][strt] = minPalindrome
    return minPalindrome


pprint.pprint(minCut("abbba"))
pprint.pprint(minCut("beebe"))
pprint.pprint(minCut("abaccdeafaed"))
pprint.pprint(minCut("a"))
pprint.pprint(minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"))
