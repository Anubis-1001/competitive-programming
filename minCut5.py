import pprint

def minCut(s):
    leastPalindromes=[2001]*len(s)
    dpPalindrome=[False]*len(s)

    for l in range(len(s)):
        least=2001
        for p in range(l+1):
            dpPalindrome[p]=s[l]==s[p]
            if l-p >=2:
                dpPalindrome[p]&=dpPalindrome[p+1]
            if dpPalindrome[p]:
                if p >0:
                    least=min(least, leastPalindromes[p-1]+1)
                else:
                    least=1

        leastPalindromes[p]=least

    return leastPalindromes[len(s)-1]

pprint.pprint(minCut("abbba"))
pprint.pprint(minCut("beebe"))
pprint.pprint(minCut("abaccdeafaed"))
pprint.pprint(minCut("a"))
pprint.pprint(minCut("adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"))
