n, x, cnt = int(input()), int(input()), 0
l = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        l.append(i * j)
for i in range(len(l)):
    if l[i] == x:
        cnt += 1
print(cnt)