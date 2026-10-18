#Problem15:
#https://www.hackerrank.com/challenges/game-of-thrones/problem
from collections import Counter

def gameOfThrones(s):
    letter_counts = Counter(s).values()
    odd_counts = [count for count in letter_counts if count % 2 != 0]
    return "YES" if len(odd_counts) <= 1 else "NO"

if __name__ == '__main__':
    s = input()
    result = gameOfThrones(s)
    print(result)
