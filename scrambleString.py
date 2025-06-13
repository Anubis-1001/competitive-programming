import time

def isScramble(s1, s2):
    if( s1 == s2 ):
        return True
    if( len(s1) == 1 ):
        return False
    result = False
    end = len(s1)
    if end > 1:
        end-=1
    for i in range(1, end):
        s1_sorted = sorted(s1[:i])
        if ( s1_sorted == sorted(s2[:i]) ):
            result = isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]) 
        if ( s1_sorted == sorted(s2[-i:]) ):
            result = result or ( isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i]) )
        if result:
            return True
    return False

print(isScramble("eebaacbcbcadaaedceaaacadccd", "eadcaacabaddaceacbceaabeccd"))
