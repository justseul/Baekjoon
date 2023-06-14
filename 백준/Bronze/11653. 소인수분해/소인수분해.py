n = int(input())

while(1):
  if n == 1 or n == 0 :
    break
  else:
    for i in range(2,n+1):
      if n % i == 0:
        n = int(n / i)
        print(i)
        break
    