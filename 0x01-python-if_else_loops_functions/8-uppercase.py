#!/usr/bin/python3
# 8-uppercase.py

def uppercase(str):
    result = ""
    for char in str:
        if 97 <= ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
    print(result)
