st = set()
s = input()
for i in s:
    st.add(i)
if(len(st) % 2 == 1):
    print('IGNORE HIM!')
else:
    print('CHAT WITH HER!')