# -*- coding: utf-8 -*-

primeNumber_arr = [2, ]
num = 3

def is_primeNumber(n):
    for x in primeNumber_arr:
        if n % x == 0:
            return False
    return True


while True:

    if is_primeNumber(num):
        primeNumber_arr.append(num)
    num += 1

    if len(primeNumber_arr) == 10001:
        print(primeNumber_arr[-1])
        break