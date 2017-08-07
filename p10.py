# -*- coding: utf-8 -*-

MAX_NUM = 2000000

my_list = list(range(2, MAX_NUM))

for x in my_list:
    print(x)
    for y in range(x * 2, MAX_NUM, x):
        try:
            my_list.remove(y)
        except Exception as e:
            pass
        print(y)

print(sum(my_list))
