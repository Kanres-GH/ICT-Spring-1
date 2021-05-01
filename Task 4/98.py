def int2hex(s, base = 16):
    res = ''
    s = int(s)
    while s:
        s, d = divmod(s, base)
        sd = str(d) if d < 10 else str(chr(ord('A')+d-10))
        res = sd + res
    return f'Int2Hex: {res}' 
def hex2int(s):
    return f'Hex2Int: {int(s, 16)}'

s = input('Input: ').lower()
print(int2hex(s))
print(hex2int(s))