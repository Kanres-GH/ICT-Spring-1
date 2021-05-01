from random import randint
def dice():
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    return d1 + d2
expected = {2 : 1/36, 3 : 2/36, 4 : 3/36, 5 : 4/36, 6 : 5/36, 7 : 6/36, 8 : 5/36, 9 : 4/36, 10 : 3/36, 11 : 2/36, 12 : 1/36}
cnt = {2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0}
for i in range(1000):
    sum = dice()
    cnt[sum] += 1
print("Total     Simulated   Expected\n          Percent    Percent")
for i in cnt:
    print("%5d %11.2f %8.2f" % (i, cnt[i] / 1000 * 100, expected[i] * 100))