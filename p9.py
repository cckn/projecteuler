# -*- coding: utf-8 -*-
c = 1

while True:
    for a in range(1, c):
        for b in range(1, c):
            if c ** 2 == a**2 + b**2 and a + b + c == 1000:
                print(a * b * c)
    c += 1
