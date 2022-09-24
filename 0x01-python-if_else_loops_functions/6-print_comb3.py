#!/usr/bin/python3
for j in range(10):
    for k in range(10):
        if j == 8 and k == 9:
            print('{}{}'.format(j, k))
        elif j != k and k > j:
            print('{}{}'.format(j, k), end='')
