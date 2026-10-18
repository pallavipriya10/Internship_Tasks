#Problem12:making Anagrams
#https://www.hackerrank.com/challenges/making-anagrams/problem
from collections import Counter
a = Counter(input().strip())
b = Counter(input().strip())
deletions = sum((a - b).values()) + sum((b - a).values())
print(deletions)
