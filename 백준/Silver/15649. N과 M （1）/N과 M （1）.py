import sys

input = sys.stdin. readline

n, m = map(int, input().split())
check = [False] * (n+1)
rs = list()
def BP(x):
    if x == m:
        print(' '.join(map(str, rs)))
        return


    for i in range(1,n+1):
        if check[i] == False:
            check[i] = True
            rs.append(i)
            BP(x+1)
            check[i] = False
            rs.pop()


BP(0)
