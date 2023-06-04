while(1):
    n1, n2 = map(int,input().split())

    if n1 == 0 and n2 == 0:
        break
    else:
        if n2 % n1 == 0:
            print("factor")
        elif n1 % n2 == 0:
            print("multiple")
        else:
            print("neither")

