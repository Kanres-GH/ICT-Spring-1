result = ''
q = int(input('Input a decimal number: '))
while q!=0:
    r = q % 2
    result+=str(r)                          #   Алгоритм из условия
    q//=2
print(f'A binary of {q} is {result[::-1]}.')