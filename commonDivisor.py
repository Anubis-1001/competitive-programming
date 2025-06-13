def commonDiv(str1, str2):
    if str1+str2 != str2+str1:
        return ""
    g = max(0, gcd(len(str1), len(str2)))

    sub = str1[:g]
    return sub
    
def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return gcd(num2, num1 % num2)


print(commonDiv("ABCABC", "ABC"))
