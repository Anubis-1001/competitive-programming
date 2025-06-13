import re

def isMatch(s, p):
    expr=re.split(r'\*+',p+"*X")[:-1]
    if p[-1]=="*":
        expr.append("-1")

    start=0
    for e in range(0, len(expr)):
        flag=True
        if expr[e] == "-1":
            return True
        if start >= len(s)-len(expr[e])-1:
            return False
        while start < len(s)-len(expr[e])-1 and flag:
            for l in range(0, len(expr[e])):
                if expr[e][l]!="." and expr[e][l]!=s[start+l]:
                    if e==0:
                        return False
                    start+=1
                    break
                if l == len(expr[e])-1:
                    start+=l+1
                    flag=False

    return True

#print(isMatch("sfsf", "s*f"))
print(isMatch("sfsf", "s*ff"))
print(isMatch("sfsf", "s*f"))
print(isMatch("sfsf", "s*s*"))
print(isMatch("abcddef", "a*dc*i"))
