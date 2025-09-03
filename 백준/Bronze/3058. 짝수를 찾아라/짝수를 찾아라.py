import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    numbers = list(map(int, input().split()))
    even_numbers = []
    
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i) 
    
    print(sum(even_numbers), min(even_numbers))