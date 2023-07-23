# TpE2EfEdTpi3EpXrTZi1SJA1TCE0SfAfSfOfSJSeSfS3FJOcTfq2Fpi1TfO0UZW0S2KfSpScSfOfSpSfSfGfSfSdSfqfSG==

import base64

def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 97 if char.islower() else 65
            ascii_code = ord(char)
            shifted_code = ((ascii_code - ascii_offset - shift) % 26) + ascii_offset
            shifted_char = chr(shifted_code)
            result += shifted_char
        else:
            result += char
    return result

def brute_force_decrypt(text):
    for shift in range(26):  # 尝试所有可能的位移量
        decrypted_text = decrypt(text, shift)
        try:
            decoded_text = base64.b64decode(decrypted_text).decode('utf-8')
            print("尝试位移量：", shift)
            print("解密后的文本：", decoded_text)
            ascii_output = ""
            for i in range(0, len(decoded_text), 2):
                hex_code = decoded_text[i:i+2]
                try:
                    ascii_char = chr(int(hex_code, 16))
                    ascii_output += ascii_char
                except ValueError:
                    pass  # 忽略数值错误
            print("转换为ASCII：", ascii_output)
        except (UnicodeDecodeError, ValueError):
            pass  # 忽略解码错误和数值错误


encrypted_text = input("请输入要解密的文本：")
brute_force_decrypt(encrypted_text)

