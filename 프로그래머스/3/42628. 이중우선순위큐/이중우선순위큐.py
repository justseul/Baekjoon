def solution(operations):
    queue = list()
    for i in operations:
        code, num = i.split()
        if code =='I':
            queue.append(int(num))
        elif code =='D' and num == '1':
            if not queue: continue
            else: queue.remove(max(queue))
        elif code =='D' and num == '-1':
            if not queue: continue
            else: queue.remove(min(queue))
            
    if queue: return [max(queue), min(queue)]
                      
    else: return [0,0]