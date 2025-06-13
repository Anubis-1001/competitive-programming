

def shortestPalindrome(s):
    i = len(s) -1
    inv_i = 0
    cycle_length = 0

    while ( i >= 0):
        if s[i] == s[inv_i]:
            if s[i+cycle_length] != s[i]:
                cycle_length = 0
            if cycle_length < 1 and s[inv_i + i] == s[i]:
                cycle_length = inv_i
            inv_i += 1
                
        else:
            if cycle_length > 0:
                inv_i -= cycle_length 
                i+=1
            else:
                inv_i = 0
        i-=1
    print(s[inv_i:][::-1]+s)

shortestPalindrome("abcd")
#print(len("cacaroyyoracac"))
