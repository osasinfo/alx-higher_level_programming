#!/usr/bin/python3
def uppercase(str):
    for alphabet in str:
        if ord(alphabet) >= 97 and ord(alphabet) <= 122:
            alphabet = ord(alphabet) - 32
        print('{}'.format(ord(alphabet), end=''))
    print('')
