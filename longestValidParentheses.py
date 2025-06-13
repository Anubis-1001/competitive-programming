def longestValidParentheses(s):
    stack=[]
    for i in range(0, len(s)):
        stack.append(i)
        if len(stack) > 1:
            if s[stack[-2]] + s[stack[-1]] == "()":
                    stack.pop()
                    stack.pop()

    max_stack=0
    stack.insert(0,-1)
    stack.append(len(s))
    for x in range(0, len(stack)-1):
        max_stack =max(stack[x+1]-stack[x]-1, max_stack)

    #return max_stack
    return stack


print(longestValidParentheses(")()())"))
print(longestValidParentheses("(()"))
print(longestValidParentheses("())"))
