#Problem19:Weighted Uniform String
#https://www.hackerrank.com/challenges/weighted-uniform-string/problem
s = input().strip()
n = int(input())
queries = [int(input()) for _ in range(n)]
weights = set()
current_char = ""
current_weight = 0
for ch in s:
    if ch == current_char:
        current_weight += ord(ch) - ord("a") + 1
    else:
        current_char = ch
        current_weight = ord(ch) - ord("a") + 1
    weights.add(current_weight)
for value in queries:
    print("Yes" if value in weights else "No")
