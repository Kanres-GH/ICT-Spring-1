def reverseLookup(data, value):
    l = [] 
    for i in data:
        if data[i] == value:
            l.append(i)
    return l
s = input()
d = {"Key 1" : "Value", "Key 2" : "Test", "Key 3" : "Apple", "Key 4" : "Bananas"}
print("Словарь:", d)
print("Найденные ключи:", reverseLookup(d, s))