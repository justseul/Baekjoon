n = int(input())
answer = 2

for i in range(1,n+1):
    answer = 2*answer-1
    if i == n:
      print((answer)**2)

