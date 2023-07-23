import itertools
L = 8
perm = [0, 1, 2, 3, 4, 5, 6, 7]
#将perm全排列
permutations = list(itertools.permutations(perm))

for p in permutations:
    msg='flag{012345678901234567890123456789};;;;;;;;;;;;'
    # 原加密部分
    for i in range(0, 100):
        msg = msg[1:] + msg[:1]
        msg = msg[0::2] + msg[1::2]
        msg = msg[1:] + msg[:1]
        res = ""
        for j in range(0, len(msg), L):
            for k in range(0,L):
                res += msg[j:j+L][p[k]]
        msg = res

    # __Ic3W4w01A3;;9fmNla6;f;_}ga;O7_3Tl;z;;765;{;;;S

    if msg[26] == 'g' and msg[43] == '{' and msg[25] == '}':
        print (msg)
        open('flag.txt','a').write(msg+' '+str(p)+'\n')