while(1):
    n = int(input())
    sum = 0
    l = []

    if n == -1:
        break

    for i in range(1,n):
        if n % i == 0:
            l.append(str(i))
            sum += i
    
    if sum == n:
        print(f"{n} = ", end = "")
        for j in range(len(l)):
            if j == len(l)-1:
                print(l[j])
            else:
                print(f"{l[j]} + ", end ="")
    else:
        print(f"{str(n)} is NOT perfect.")
