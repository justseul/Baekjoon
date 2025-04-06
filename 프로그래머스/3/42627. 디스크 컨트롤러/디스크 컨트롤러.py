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

# def solution(jobs):
#     waitQueue = list() # 작업 시간-, 요청 시각+, 작업 번호-
#     disk = list()
#     time = 0
#     start = 0
#     while(1):
#         if jobs[0][0] == time:
#             waitQueue.append(jobs.pop(0))
#         sorted(waitQueue, key = lambda x : (x[1], -x[0], waitQueue.index(x)))
#         if not disk and not waitQueue: 
#             now = waitQueue.pop(0)
#             disk.append(now)
#             dt = disk[0][1]
#             start = time
#         if disk and time - start == dt:
#             disk.pop(0)
#             continue
#         time += 1
#     return time/len(jobs)