# print('input >>')
K, N = map(int,(input().split()))
As = list(map(int,(input().split())))

As = [A - As[0] for A in As]
As_diffs = [As[i+1] - As[i] for i in range(len(As)-1)]
As_diffs += [K - As[-1]]
As_fiff_max = max(As_diffs)

# print('-----output-----')
print(K - As_fiff_max)