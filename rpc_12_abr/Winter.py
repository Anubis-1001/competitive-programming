year_1, year_2 = map(int, input().split(" ") )

total=0

x=0
while x*x <= year_2:
    if year_1 <= x*x <= year_2:
        total+=15
    x+=1

print(total)


