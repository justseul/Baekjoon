def solution(N, number):
    
    if number == N:
        return 1
    n_list = [set() for _ in range(8)]
    answer = -1
    for i in range(8):
        n_list[i].add(int(str(N)*(i+1)))
    
    for i in range(1, 8):
        for j in range(i):
            for op1 in n_list[j]:
                for op2 in n_list[i-j-1]:
                    n_list[i].add(op1+op2)
                    n_list[i].add(op1-op2)
                    n_list[i].add(op1*op2)
                    if op2 != 0:
                        n_list[i].add(op1//op2)
        if number in n_list[i]:
            answer = i+1
            break
            
    print(n_list)
    return answer