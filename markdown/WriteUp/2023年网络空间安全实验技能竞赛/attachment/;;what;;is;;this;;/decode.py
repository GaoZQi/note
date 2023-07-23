L = 8
# 原perm = [5, 0, 3, 7, 4, 1, 6, 2]
# 求逆perm = [1, 5, 7, 2, 4, 0, 6, 3]
perm = [1, 5, 7, 2, 4, 0, 6, 3]
# 密文
encrypted_msg = "__Ic3W4w01A3;;9fmNla6;f;_}ga;O7_3Tl;z;;765;{;;;S"
# 明文
msg = ''

for i in range(100):
    msg=''
    # 第一步将密文按照求逆perm的顺序排列
    for j in range(0,len(encrypted_msg),L):
        for k in range(L):
            msg += encrypted_msg[j:j+L][perm[k]]

    # 第二步将密文左移一位
    msg = msg[47:] + msg[:47]
    encrypted_msg = msg
    
    # 将密文前24与后24交错拼接
    msg=''
    for s in range(0,24):
        msg += encrypted_msg[s]+encrypted_msg[s+24]
    
    # 将密文左移一位
    msg = msg[47:] + msg[:47]
    encrypted_msg = msg

print(msg.strip(";"))
