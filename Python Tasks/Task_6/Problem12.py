#Problem12:Set .discard(), .remove() & .pop() 
#https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
n = int(input())
s = set(map(int, input().split()))
q = int(input())
for _ in range(q):
    command = input().split()
    if command[0] == "pop":
        if s:
            s.pop()
    elif command[0] == "remove":
        s.remove(int(command[1]))
    elif command[0] == "discard":
        s.discard(int(command[1]))
print(sum(s))

