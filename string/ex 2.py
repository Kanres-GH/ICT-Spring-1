s = input().lower()
symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '+', '-', '.', ',', '/', ':', '!', '?', '*']
l = []
for i in range(len(symbols)):
    if s.count(symbols[i])!=0:
        l.append(symbols[i])
        l.append(s.count(symbols[i]))
print(*l[0:len(l):2])
print(*l[1:len(l):2])