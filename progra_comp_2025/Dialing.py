line = input().split(" ")
t_words = int(line[0])
t_numbers = int(line[1])

list_of_words = []
list_of_numbers = []
for _ in range(t_words):
    list_of_words.append(input())

for _ in range(t_numbers):
    list_of_numbers.append(input())

def getCode(word):
    code=""
    for l in word:
        h = ord(l) - ( 1 if l in "svyz" else 0) - ( 1 if l=="z" else 0)
        code+=str((h-91)//3)
    return code


def getDialing(list_words, list_numbers):
    word="bapc"
    code_arr = []
    for word in list_words:
        code_arr.append(getCode(word))


    for n in list_numbers:
        result=""
        count=0
        for word in list_words:
            if getCode(word) == n:
                count+=1
                result+=" "+word
        print(str(count)+" "+result)


getDialing(list_of_words, list_of_numbers)
