A, B = input().split()

new_A = []
new_B = []

for i in range(2, -1, -1):
    new_A.append(A[i])
    new_B.append(B[i])
new_A = int("".join(new_A))
new_B = int("".join(new_B))

if(new_A > new_B):
    print(new_A)
else:
    print(new_B)