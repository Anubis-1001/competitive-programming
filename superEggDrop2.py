def superEggDrop(k, n):
    return superEggDropRecursive(k, n, 0)

def superEggDropRecursive(k, n, dropCount):
    #print("+++", k, n)
    if k==1:
        #print("by n", n+dropCount)
        return n+dropCount
    if n<=3:
        #print("byDropCount", dropCount+min(2, n) )
        return dropCount+min(2, n)
    elif 2**(k+1)-2 <= n:
        #print("at k=2")
        return max(superEggDropRecursive(k-1, n//2-1, dropCount+1), superEggDropRecursive(k, (n+1)//2, dropCount+1))
    else:
        #print("at k>2")
        return max(superEggDropRecursive(k-1, n//2, dropCount+1), superEggDropRecursive(k, (n-1)//2, dropCount+1))

print(superEggDrop(1, 2))
print(superEggDrop(2, 6))
print(superEggDrop(3, 14))
print(superEggDrop(3, 4))
print("k=2")
print(superEggDrop(2, 2))
print(superEggDrop(2, 3))
print(superEggDrop(2, 4))
print(superEggDrop(2, 5))
print(superEggDrop(2, 6))
print(superEggDrop(2, 7))
print(superEggDrop(2, 10))
#print(superEggDrop(3, 14))
#print(superEggDrop(3, 15))

