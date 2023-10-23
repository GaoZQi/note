import base64
import random
import flag from *

def caesar_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            shifted = ord(char) + shift
            if shifted > ord('z'):
                shifted -= 26
            encrypted_char = chr(shifted)
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def rail_fence_encrypt(plain_text, rails):
    matrix = [['' for _ in range(len(plain_text))] for _ in range(rails)]
    down = False
    row, col = 0, 0
    for char in plain_text:
        if row == 0 or row == rails - 1:
            down = not down
        matrix[row][col] = char
        col += 1
        if down:
            row += 1
        else:
            row -= 1
    encrypted_text = ''.join([''.join(row) for row in matrix])
    return encrypted_text


original_text = ????????????????????????
caesar_shift = random.randint(1, 25)
rail_fence_rails = random.randint(2, 10)
caesar_encrypted_text = caesar_encrypt(original_text, caesar_shift)
rail_fence_encrypted_text = rail_fence_encrypt(caesar_encrypted_text, rail_fence_rails)
base64_encoded_text = base64.b64encode(rail_fence_encrypted_text.encode('utf-8')).decode('utf-8')
base32_encoded_text = base64.b32encode(base64_encoded_text.encode('utf-8')).decode('utf-8')
