def solution(arr):
    answer = []
    
    for i in range(len(arr)-1):
        
        if(arr[i] == arr[i+1]):
            pass
        else:
            answer.append(arr[i])
    answer.append(arr[-1])
    
    return answer