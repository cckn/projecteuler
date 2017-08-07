
num = 1


def is_passed(n):
    for x in range(1, 21):
        if num % x:
            return False
    return True

while True:
    if is_passed(num):
        print(num)
        break
    else:
        num += 1
