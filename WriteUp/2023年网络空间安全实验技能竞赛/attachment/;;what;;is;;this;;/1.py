import random
 
L = 8
perm = range(L)
random.shuffle(perm)
 
msg = open("/flag").read().strip()
while len(msg) % (2*L):
    msg += ";"
 
for i in xrange(100):
    msg = msg[1:] + msg[:1]
    msg = msg[0::2] + msg[1::2]
    msg = msg[1:] + msg[:1]
    res = ""
    for j in xrange(0, len(msg), L):
        for k in xrange(L):
            res += msg[j:j+L][perm[k]]
    msg = res
print (msg)