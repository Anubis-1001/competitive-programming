corns = list(map(int, input().split(" ")))
N, KWF = list(map(int, input().split(" ")))

avg = 0
for i in range(len(corns)//2):
    avg+=corns[2*i]*corns[2*i+1]

avg//=5


print(avg*N//KWF)
