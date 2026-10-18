#Problem14.py:Anagram
#https://www.hackerrank.com/challenges/anagram/problem
from collections import Counter
def anagram(s):
    if len(s) % 2:
        return -1
    half = len(s) // 2
    left = Counter(s[:half])
    right = Counter(s[half:])
    return sum((left - right).values())
q = int(input())
for _ in range(q):
    print(anagram(input().strip()))
