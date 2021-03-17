import heapq

# print('input >>')
X, Y, A, B, C = map(int,(input().split()))
ps = list(map(int,(input().split())))
qs = list(map(int,(input().split())))
rs = list(map(lambda x:int(x)*-1,(input().split())))

ps.sort()
qs.sort()
rs.sort()

ps = ps[-X:]
qs = qs[-Y:]

heapq.heapify(ps)
heapq.heapify(qs)
heapq.heapify(rs)

while True:
    if len(rs) == 0:
        break
    max_r = heapq.heappop(rs)
    min_p = heapq.heappop(ps)
    min_q = heapq.heappop(qs)

    min_pq = min(min_p, min_q)

    if max_r*-1 > min_pq:
        if min_p < min_q:
            heapq.heappush(ps, max_r*-1)
            heapq.heappush(qs, min_q)
        else:
            heapq.heappush(qs, max_r*-1)
            heapq.heappush(ps, min_p)
    else:
        heapq.heappush(qs, min_q)
        heapq.heappush(ps, min_p)
        break

# print('-----output-----')
print(sum(ps) + sum(qs))