def longestPath(parent, s):
    childs=[ [] for _ in parent ]
    for i in range(len(parent)):
        if i != 0: childs[parent[i]].append(i)

    #print(childs)
    def dfs(i):
        longest=[0, 0]
        maximum=float("-inf")

        for x in childs[i]:
            r=dfs(x)
            if s[i] != s[x]:
                lb=max(r[0])
                if lb > longest[0]:
                    longest = [lb, longest[0]]
                elif lb > longest[1]:
                    longest = [longest[0], lb]
            maximum=max(maximum, sum(r[0]), r[1])

        maximum=max(maximum, sum(longest)+2)
        return [ longest[0]+1, longest[1]+1], maximum

    #buffer=[0]
    #string="0"
    #while buffer:
    #    #for i in buffer:
    #     #   string+=s[i]+", "
    #    print(string)
    #    string=""
    #    buffer2=[]
    #    for n in buffer:
    #        buffer2+=childs[n]
    #        for x in childs[n]:
    #            string+=s[x]+", "
    #        string+="   "
    #    buffer=buffer2
    return dfs(0)[1]-1


print(longestPath([-1,0,0,1,1,2], "abacbe"))
print(longestPath([-1,0,0,0], "aabc"))
print(longestPath([-1,0,1], "aab"))
print(longestPath([-1,137,65,60,73,138,81,17,45,163,145,99,29,162,19,20,132,132,13,60,21,18,155,65,13,163,125,102,96,60,50,101,100,86,162,42,162,94,21,56,45,56,13,23,101,76,57,89,4,161,16,139,29,60,44,127,19,68,71,55,13,36,148,129,75,41,107,91,52,42,93,85,125,89,132,13,141,21,152,21,79,160,130,103,46,65,71,33,129,0,19,148,65,125,41,38,104,115,130,164,138,108,65,31,13,60,29,116,26,58,118,10,138,14,28,91,60,47,2,149,99,28,154,71,96,60,106,79,129,83,42,102,34,41,55,31,154,26,34,127,42,133,113,125,113,13,54,132,13,56,13,42,102,135,130,75,25,80,159,39,29,41,89,85,19] , "ajunvefrdrpgxltugqqrwisyfwwtldxjgaxsbbkhvuqeoigqssefoyngykgtthpzvsxgxrqedntvsjcpdnupvqtroxmbpsdwoswxfarnixkvcimzgvrevxnxtkkovwxcjmtgqrrsqyshxbfxptuvqrytctujnzzydhpal"))
print(longestPath([-1,17,37,80,9,16,12,78,63,8,29,30,71,16,5,80,62,14,71,41,9,13,31,80,36,18,66,62,62,39,5,56,80,27,71,37,69,36,28,47,78,28,21,78,17,39,7,71,39,22,58,66,66,54,27,56,78,9,27,9,78,40,63,36,75,63,27,50,10,0,11,80,24,5,42,47,18,69,36,25,27], "oozbypewdgpayutsufzpctovgkqrofjimkeckfzgvziqohymdtuppjcuytygjzlagiowhrfcjntjbbwru"))
