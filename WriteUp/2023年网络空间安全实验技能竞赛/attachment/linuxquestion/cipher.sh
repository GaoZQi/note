#!/bin/bash

# 加密函数
_cipher() {
    local text="$1"
    local shift="$2"
    local result=""
    for ((i=0; i<${#text}; i++)); do
        char="${text:i:1}"
        if [[ "$char" =~ [a-zA-Z] ]]; then
            if [[ "$char" =~ [a-z] ]]; then
                ascii_offset=97
            else
                ascii_offset=65
            fi
            ascii_code=$(printf "%d" "'$char")
            shifted_code=$(((ascii_code - ascii_offset + shift) % 26 + ascii_offset))
            shifted_char=$(printf "\\$(printf '%03o' "$shifted_code")")
            result+="$shifted_char"
        else
            result+="$char"
        fi
    done

    echo "$result"
}

# 加密明文
encrypt_plaintext() {
    local plaintext="$1"
    local encoded_text=$(echo -n "$plaintext" | xxd -p | tr -d '\n')
    local encrypted_text=$(echo "$encoded_text" | base64 | tr -d '\n')
    local ciphertext=$(_cipher "$encrypted_text" 15)
    echo "$ciphertext"
}

# 主函数
main() {
    read -p "请输入明文: " plaintext
    ciphertext=$(encrypt_plaintext "$plaintext")
    echo "加密得到的密文: $ciphertext"
}

# 执行主函数
main