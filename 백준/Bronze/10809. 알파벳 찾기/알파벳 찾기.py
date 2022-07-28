from string import ascii_lowercase
alphabet_list = list(ascii_lowercase)
S = list(input())

for i in alphabet_list:
    if i in S:
        print(S.index(i))
    else:
        print(-1)