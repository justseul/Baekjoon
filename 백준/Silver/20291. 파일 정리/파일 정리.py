import sys
input = sys.stdin.readline

n = int(input())
extension = {}

for _ in range(n):
    filename = input().strip()
    name, ext = filename.split('.')
    if ext in extension:
        extension[ext] += 1
    else:
        extension[ext] = 1

for ext, count in sorted(extension.items()):
    print(ext, count)
