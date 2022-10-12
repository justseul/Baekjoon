def self_Number(n): 
    number = n 
    for i in list(str(n)): 
        number += int(i) 
    return number 

list1 = [] 

for i in range(10000): 
    list1.append(self_Number(i)) 

for j in range(10000): 
    if j in list1: 
        pass 
    else:
        print(j) 