from functools import lru_cache

def smallestSufficientTeam(req_skills, people):
    n = len(req_skills)
    skills_idx = [ i for i in range(n) ]
    bitmask = (1<<n) - 1
    people_bitmask = []
    for p in people:
        bitmask_people = 0
        for skills in p:
            i = req_skills.index(skills)
            if i != -1:
                bitmask_people+= 1 << i
        people_bitmask.append(bitmask_people)

    people_index = [ i for i in range(len(people)) ]

    @lru_cache(None)
    def dfs(people_idxs, mask, n):
        if mask == 0: return 0
        l_min = 0
        for idx in range(len(people_idxs)):
            l_arr = people_idxs[:idx]+people_idxs[idx+1:]
            l_mask = mask & ~people[people_idxs[idx]]
            l_min = min( l_min, dfs(l_arr, mask) )

        return l_min+0

    print(people_index)
    dfs(people_index, bitmask, n)

print(smallestSufficientTeam(["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]))
