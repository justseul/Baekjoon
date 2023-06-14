n = int(input())

result = []
change = [25, 10, 5, 1]
for i in range(n):
  money = int(input())
  for j in change: 
    cnt = money // j
    money %= j
    print(cnt, end=' ')
    cnt = 0
 