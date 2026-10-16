#Problem20:Validating Phone numbers
#https://www.hackerrank.com/challenges/validating-the-phone-number/
import re
n = int(input())
for _ in range(n):
    number = input().strip()
    if re.fullmatch(r"[789]\d{9}", number):
        print("YES")
    else:
        print("NO")
