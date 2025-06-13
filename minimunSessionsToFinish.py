class Solution:
    def minSessions(self, tasks: list[int], sessionTime: int) -> int:
        count=0
        selected=0
        n=len(tasks)
        while selected < 2**n-1:
            temp=self.getMaximumPerSession(selected, tasks, sessionTime, 0)
            selected=temp
            count+=1

        return count

    def getMaximumPerSession(self, selected, tasks, sessionTime, total):
        print(selected)
        if total == sessionTime:
            return selected
        elif total > sessionTime or selected >= 2**len(tasks)-1:
            return -1

        greatest=-1
        selected_result=selected
        for n in range(selected & (~selected), len(tasks)):
            if selected & 1<<n == 0:
                new_selected=selected | 1<<n
                res=self.getMaximumPerSession(new_selected, tasks, sessionTime, total+tasks[n])
                sum_res=sum([tasks[i] for i in range(0, len(tasks)) if new_selected & 1<<i])
                if sum_res > greatest:
                    greatest = sum_res
                    selected_result=res

        return selected_result


sol=Solution()
sol.minSessions([3,1,3,1,1], 8)
sol.minSessions([1,2,3], 3)
sol.minSessions([1,2,3,4,5], 15)
