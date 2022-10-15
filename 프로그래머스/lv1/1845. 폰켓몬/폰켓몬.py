def solution(nums):
    dic = {}
    
    for i in nums:
        dic[i] = hash(i)
        
    if len(dic) >= len(nums)/2:
        return len(nums)/2   
    else:
        return len(dic)    