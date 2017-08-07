
num = 20


def is_divisible(n):
    for x in range(1, 20):
        if num % x:
            return False
    return True

while True:
    if is_divisible(num):
        print(num)
        break
    else:
        num += 20
