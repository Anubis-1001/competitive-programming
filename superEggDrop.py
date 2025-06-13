def superEggDrop(k, n):
    l=n
    h=n
    drops=0
    dropH=0
    while k > 1 and l > 0:
        l=(l//2)-1
        k-=1
        drops+=1

    while h > 0:
        if h == 3: 
            h=0
            dropH+=2
        else:
            if h ==1: h=0
            h=h-h//2
            dropH+=1
        
    print(">>", drops+max(0,l))
    print(">>", dropH)
    return max(drops+max(0, l), dropH)

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
print(superEggDrop(3, 14))

