#t = int(input())

#for _ in range(t):
 #   number = input()

def next_one(s, p):
    d=s[len(s)-p]
    n_n=str(int(s)+1)
    if n_n[len(s)-p] != d:
        if p == 1:
            n_n = int(n_n)//10
            if n_n % 10 == int(d): return str(n_n*10), 2
            n_n+=1
            power = 1
            while n_n % 10**power == 0: power+=1
            digit = n_n//( 10**power//10 )
            if digit % 10 == int(d): return str(n_n*10), power+1
            else: return str(n_n*10+int(d)), 1

        else: return str(int(n_n)+int(d)), 1

    else: return n_n, p

def length(number):
    count=0
    for i in range(0, len(number)):
        if i == len(number)-1:
            count+=(i+1)*( int(number) - (10**i-1) )
        else:
            count+= (i+1)*(10**i)*9

    return count


def check(pattern, pivot, number, index):

    if length(number) < pivot:
        return False

    identation = "?"*( len(number)-index-pivot )

    pattern=identation + pattern

    number_expanded = ""
    while len(number_expanded) <= len(pattern):
        number_expanded+=number
        number=str(int(number)+1)

    for i in range(len(pattern)):
        if pattern[i] != "?" and pattern[i] != number_expanded[i]:
            return False

    return True



pat = "1?1?1" ## to change
pvt = 0
for i in range(len(pat)):
    if pat[i] == "?":
        pvt+=1
    else:
        break

num, ind = pat[pvt], 1
while not check(pat, pvt, num, ind):
    num, ind = next_one(num, ind)


print(num, ind)

#print(length("121"))
#print(ind, num)
#print(next_one("110", 1))
#print(check("121", 0, "12", 2))
#print(check("?9???8", 1, "197", 2))

#print(next_one("189", 1))
