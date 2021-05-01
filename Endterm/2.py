y = int(input())
while(True):
    y += 1
    y1 = y//1000
    y2 = y//100%10
    y3 = y//10%10
    y4 = y%10
    if y1 != y2 and y1 != y3 and y1 != y4 and y2 != y3 and y2 != y4 and y3 != y4:
        break
print(y)