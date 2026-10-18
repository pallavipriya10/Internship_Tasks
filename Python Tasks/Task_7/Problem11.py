#Problem11:Two-Strings
#https://www.hackerrank.com/challenges/two-strings/problem
def twoStrings(s1, s2):
    if len(set(s1).intersection(set(s2))) >= 1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
