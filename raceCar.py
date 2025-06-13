def racecar(target):
    steps=0
    binary=bin(target)[2:]
    i=0
    while i < len(binary):
        if binary[i]=="0":
            steps+=len(binary)+(len(binary)-i)+1
            binary=binary[i:]
            indx=binary.index('1') if '1' in binary else -1
            binary=binary[binary.index("1"):] if indx > -1 else ""
            i=-1
        i+=1

    if i >0:
        steps+=len(binary)

    return steps


print(racecar(7))
print(racecar(1))
print(racecar(3))
print(racecar(6))
print(racecar(10))
print(racecar(4))

