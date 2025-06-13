def longestValidParentheses(s):
    stack=[0]
    for i in range(0, len(s)):
        stack.append(0)
        if i > 2:
            if s[stack[-2]+len(stack)-2] + s[stack[-1]+len(stack)-1] == "()":
                    stack[-3]=stack.pop()+stack.pop()+2

    max_stack=max(stack)
    return stack


print(longestValidParentheses(")()())"))
print(longestValidParentheses("(()"))

