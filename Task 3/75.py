a = int(input())
b = int(input())
d = min(a,b)
while a%d!=0 or b%d!=0:         #       Алгоритм из условия
        d-=1
print(d)