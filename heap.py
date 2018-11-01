import heapq

H= [21,1,45,78,3,5]
heapq.heapify(H)
print(H)

heapq.heappush(H,0)
heapq.heapify(H)
print(H)

heapq.heappop(H)
print(H)