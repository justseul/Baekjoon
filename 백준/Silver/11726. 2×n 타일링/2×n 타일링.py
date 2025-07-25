import sys

input  = sys.stdin.readline

n = int(input())
n_list = [0, 1, 2]
for i in range(3, n+1):
    n_list.append((n_list[i-2] + n_list[i-1])%10007)

print(n_list[n])