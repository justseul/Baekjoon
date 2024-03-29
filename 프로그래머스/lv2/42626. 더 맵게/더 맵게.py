import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while(1):
        if(len(scoville) == 1 and scoville[0] < K):
            return -1
        first = heapq.heappop(scoville)
        if(first >= K):
            return answer
        second = heapq.heappop(scoville)
        heapq.heappush(scoville,first + second*2)
        answer +=1

    return answer
