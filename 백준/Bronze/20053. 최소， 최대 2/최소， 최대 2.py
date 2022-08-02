T = int(input())

for _ in range(T):
    n = int(input())
    ele =list(map(int,input().split()))
    
    print(min(ele), max(ele))   