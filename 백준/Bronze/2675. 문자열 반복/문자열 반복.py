N = int(input())
list_1 = []
for i in range(N):
    R, S = input().split()
    

    for j in range(len(S)):
        list_1.append(S[j]*int(R))
    print(''.join(list_1))
    list_1 = []