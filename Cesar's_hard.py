en_alphabet_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_alphabet_low = 'abcdefghijklmnopqrstuvwxyz'
s = input().split()
s1 = ''
for i in s:
    count = 0
    s1 += ' '
    for j in i:
        if j.isalpha():
            count += 1
    for j in i:
        if j.isupper():
            s1 += en_alphabet_up[(en_alphabet_up.find(j) + count) % 26]
        elif j.islower():
            s1 += en_alphabet_low[(en_alphabet_low.find(j) + count) % 26]
        elif j == ' ':
            s1 += j
        else:
            s1 += j
print(s1.lstrip())
