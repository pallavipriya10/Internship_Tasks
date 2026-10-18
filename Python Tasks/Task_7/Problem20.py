#Problem20:Super reduced string
#https://www.hackerrank.com/challenges/reduced-string/problem
s = input().strip()
stack = []

for ch in s:
    if stack and stack[-1] == ch:
        stack.pop()
    else:
        stack.append(ch)
result = "".join(stack)
print(result if result else "Empty String")
