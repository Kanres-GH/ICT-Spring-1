n = int(input())
suma = sumb = sumc = 0
for i in range(n):
    num = input().split()
    suma += int(num[0])
    sumb += int(num[1])
    sumc += int(num[2])
if(suma == sumb == sumc == 0):
    print('YES')
else:
    print('NO')