import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int, input().split()))


def search(st, en, target):
    while st <= en:
        mid = (st + en) // 2
        if n_list[mid] == target:
            return 1
        elif n_list[mid] < target:
            st = mid + 1
        else:
            en = mid - 1
    return 0

for i in m_list:
    print(search(0, n-1, i))