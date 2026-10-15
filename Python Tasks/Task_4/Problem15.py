#Print the number of distinct words and their occurrence counts in order of first appearance.
#https://www.hackerrank.com/challenges/word-order/problem
from collections import OrderedDict

if __name__ == '__main__':
    n = int(input())
    words = OrderedDict()

    for _ in range(n):
        word = input().strip()
        words[word] = words.get(word, 0) + 1

    print(len(words))
    print(*words.values())

