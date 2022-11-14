def solution(brown, yellow):
    lst=[]
    dic={}

    for i in range(1, brown + yellow+1):
        if((brown + yellow) % i==0):
            lst.append(i)
    if(len(lst)%2!=0):
        lst.append(lst[len(lst)//2])
        lst = sorted(lst)
    lst1=sorted(lst,reverse=True)

    for a, b in zip(lst,lst1):
        if(a-2)*(b-2)==yellow and a>=b:
            return [a,b]
