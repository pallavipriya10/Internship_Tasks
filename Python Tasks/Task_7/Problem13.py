#Problem13:Sherlock and the valid string
#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem
from collections import Counter
s = input().strip()
freq_counts = Counter(Counter(s).values())
if len(freq_counts) == 1:
    print("YES")
elif len(freq_counts) == 2:
    items = list(freq_counts.items())
    (f1, c1), (f2, c2) = items
    if (f1 == 1 and c1 == 1) or (f2 == 1 and c2 == 1):
        print("YES")
    elif abs(f1 - f2) == 1 and ((f1 > f2 and c1 == 1) or (f2 > f1 and c2 == 1)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
