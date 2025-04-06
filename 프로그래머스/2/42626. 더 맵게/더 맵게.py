import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0

    while scoville:
        if scoville[0] >= K:
            return cnt
        if len(scoville) < 2:
            return -1

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + second * 2
        heapq.heappush(scoville, new_food)
        cnt += 1