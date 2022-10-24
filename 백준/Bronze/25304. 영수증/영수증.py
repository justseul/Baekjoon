total_money = int(input())
n = int(input())
total = 0
for i in range(n):
    price, number = map(int,input().split())
    total += price * number
if(total == total_money):
    print('Yes') 
else:
    print('No')