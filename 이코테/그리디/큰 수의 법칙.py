n,m,k = map(int, input().split())

array = list(map(int, input().split()))
array = sorted(array, reverse = 1)

first = array[0]
second = array[1]

f_n = m // k
s_n = m % k 

sum = f_n * k * first + s_n * second 
print(sum)
