n = int(input())
suma = sumb = sumc = 0
for i in range(n):
    a, b, c = map(int, input().split())
    suma += a
    sumb += b
    sumc += c
if(suma == sumb == sumc == 0):
    print('YES')
else:
    print('NO')