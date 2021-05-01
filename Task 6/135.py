cnt1 = {}
cnt2 = {}
s1 = input().lower()
s2 = input().lower()
for i in s1:
    if i in cnt1:
        cnt1[i] += 1
    else:
        cnt1[i] = 1
for j in s2:
    if j in cnt2:
        cnt2[j] += 1
    else:
        cnt2[j] = 1
if cnt1 == cnt2:
    print('Those strings are anagrams')
else:
    print('Those strings are not anagrams')