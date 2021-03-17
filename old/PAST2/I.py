# print('input >>')
N = int(input())
As = list(map(int,(input().split())))

tour = []
for i, A in enumerate(As):
    tour.append((i, A))

ans = [0] * 2**N

time = 0
while len(tour) > 1:
    time += 1
    new_tour = []
    for i in range(0, len(tour), 2):
        first = i
        second = i+1
        if tour[i][1] > tour[i+1][1]:
            new_tour.append(tour[i])
            ans[tour[i+1][0]] = time
        else:
            new_tour.append(tour[i+1])
            ans[tour[i][0]] = time
    # print(new_tour, ans)
    tour = new_tour

# print('-----output-----')
for ans_ in ans:
    if ans_ == 0:
        print(N)
    else:
        print(ans_)