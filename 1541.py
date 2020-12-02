s = input()
ret = 0
if not s[0].isdecimal():
    s = s.split('-')
    for i in range(1, len(s)):
        ret -= int(s[i])
    print(ret)
    exit()

s = s.split('-')

tmp = s[0].split('+')
for a in tmp:
    ret += int(a)

for i in range(1, len(s)):
    tmp = s[i].split('+')
    try:
        ret -= int(tmp)
    except:
        for a in tmp:
            ret -= int(a)

print(ret)