import math
a, b, v = list(map(int,input().split()))

print(math.ceil((v - a)/(a-b))+1)