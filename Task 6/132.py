address = {"Newfoundland" : "A", "Nova Scotia" : "B", 'Prince Edward Island' : 'C', 'New Brunswick' : 'E', 'Quebec' : 'G',
'Quebec' : 'H', 'Quebec' : 'J', 'Ontario' : 'K', 'Ontario' : 'L', 'Ontario' : 'M', 'Ontario' : 'N', 'Ontario' : 'P',
'Manitoba' : 'R', 'Saskatchewan' : 'S', 'Alberta' : 'T', 'British Columbia' : 'V', 'Nunavut or Northwest Territories' : 'X',
'Yukon' : 'Y'}
s = list(input().upper())
territory = ''
ex = ['D', 'F', 'I', 'Q', 'O', 'U', 'W', 'Z']
if (s[0] in ex or s[1].isdigit() == False) or len(s) != 6:
    print('Invalid postal code')
else:
    urban = True
    if s[1] == '0':
        urban = False
    for i in address:
        if s[0] == address[i]:
            territory += i
    if urban:
        print('Postal code is from an urban address.')
    else:
        print('Postal code is from a rural address.')
    print('Province/Territory:', territory)
    
