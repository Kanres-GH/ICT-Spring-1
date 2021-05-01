digits = {"one" : "1", "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" : "6", "seven" : "7", "eight" : "8", "nine" : "9"}
afterdigits = {"ten" : "10", "eleven" : "11", "twelve" : "12", "thirteen" : "13", "fourteen" : "14", "fifteen" : "15", "sixteen" : "16", "seventeen" : "17", "eighteen" : "18", "nineteen" : "19"}
tens = {"twenty" : "2", "thirty" : "3", "fourty" : "4", "fifty" : "5", "sixty" : "6", "seventy" : "7", "eighty" : "8", "ninety" : "9"}
st = input()
num = int(st)
s = list(st)
out = ''
if num == 0:
    print('zero')
else:
    for i in digits:
        if str(num // 100) == digits[i]:
            out += i + ' hundred '
    for i in tens:
        if str(num // 10 % 10) == tens[i]:
            out += i + ' '
    for i in digits:
        if (str(num % 10) == digits[i] and num % 100 > 20) or (str(num % 10) == digits[i] and num % 100 < 10):
            out += i
    for i in afterdigits:
        if str(num % 100) == afterdigits[i]:
            out += i
    print(out)