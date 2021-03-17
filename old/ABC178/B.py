a, b, c, d = map(int,(input().split()))

anss = []

anss.append(a*c)
anss.append(a*d)
anss.append(b*c)
anss.append(b*d)

print(max(anss))