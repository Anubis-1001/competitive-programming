class Solution:
  def longestValidParentheses(self, s: str) -> int:
    
    stack=[]
    for i in range(0, len(s)):
        stack.append(i)
        if i > 1:
            if s[stack[-2]] == "(" and s[stack[-1]] == ")":
                    stack.pop()
                    stack.pop()

    max_stack=0
    for x in range(0, len(stack)-1):
        max_stack =max(stack[x+1]-stack[x]-1, max_stack)
    if len(stack) > 0:
        max_stack=max(len(s)-stack[-1]-1, max_stack)
    else:
        return len(s)

    return max_stack

