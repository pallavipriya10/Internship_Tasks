#Problem5:Altenating-Characters
#https://www.hackerrank.com/challenges/alternating-characters/problem
def alternating_characters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions
t = int(input())
for _ in range(t):
    print(alternating_characters(input().strip())
