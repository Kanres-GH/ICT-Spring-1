def is_palindrome(text):
    t = txt.replace(' ', '')        #        "Игнорируем" специальные знаки 
    t = t.replace('-', '')
    t = t.replace('?', '')
    t = t.replace('!', '')
    t = t.replace('.', '')
    t = t.replace(',', '')
    t = t.lower()                   #       Делаем все буквы маленькими
    for _ in range(len(t)):
        if t[::-1] == t:            #       Если введёная строка равна перевёрнутой строке:
            return 'This string is a palindrome.'       #   Результат 1
        else:
            return 'This string is not a palindrome.'   #   Результат 2
txt = input()
print(is_palindrome(txt))