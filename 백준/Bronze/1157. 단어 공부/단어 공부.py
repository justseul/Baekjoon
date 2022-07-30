string = input().upper()
string_1 = list(set(string))
x = []

for i in string_1:
    x.append(string.count(i))
    
if(x.count(max(x)) >= 2):
    print('?')
else:
    print(string_1[x.index(max(x))])