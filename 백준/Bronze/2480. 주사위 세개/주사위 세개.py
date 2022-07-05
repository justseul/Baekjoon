F,S,T = map(int, input().split())

if(F==S and F==T ):
    cost = 10000+ F*1000
elif(F==S):
    cost = 1000+100*F
elif(S==T):
    cost = 1000+100*S
elif(F==T):
    cost = 1000+100*T
else:
    if((F>T and T>S) or (F>S and S>T)):
        cost = F*100
    elif((S>F and F>T) or (S>T and T>F)):
        cost = S*100
    elif((T>F and F>S) or (T>S and S>F)):
        cost = T*100
print(cost)        