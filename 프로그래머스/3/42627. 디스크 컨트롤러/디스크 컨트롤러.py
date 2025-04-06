import heapq

def solution(jobs):
    jobs.sort()  
    heap = []
    time = 0
    idx = 0
    total_time = 0
    count = 0
    
    while count < len(jobs):
        while idx < len(jobs) and jobs[idx][0] <= time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0])) 
            idx += 1
        
        if heap:
            job_time, req_time = heapq.heappop(heap)
            time += job_time
            total_time += time - req_time
            count += 1
        else:
            time += 1  

    return total_time // len(jobs)