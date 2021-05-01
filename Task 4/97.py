from random import randint
txt = ''
count = 0
def is_password_good(password):
    cnt = 0
    num = '0123456789'
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if len(txt)>=8:
        cnt += 1
    for i in txt:
        if i in num:
            cnt+=1
            break
    for i in txt:
        if i in lower:
            cnt+=1
            break
    for i in txt:
        if i in upper:
            cnt+=1
            break
    return cnt == 4
for i in range(8):
    txt += chr(randint(33,126))
while is_password_good(txt) == False:
    txt += chr(randint(33,126))
    count += 1
print('Number of attempts creating new password:', count)
print('Your new password is:', txt)
print('Length of your new password:', len(txt))