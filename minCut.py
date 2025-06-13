import pprint

def minCut(s):
    dpPalindrome=[[False]*len(s) for _ in s]
    dp=[[2001]*len(s) for _ in s]

    for end in range(0, len(dpPalindrome)):
        for start in range(0, end+1):
            if end==start: dpPalindrome[end][start] = True
            if end-start >= 2: dpPalindrome[end][start]=dpPalindrome[end-1][start+1] and s[start] == s[end]
            else: dpPalindrome[end][start]=s[start] == s[end]
            if dpPalindrome[end][start]: dp[end][start] = 1


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
