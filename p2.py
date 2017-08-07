# import time

result = 0

arr = [1, 2]

while True:
    next_num = arr[-1] + arr[-2]
    if next_num > 4000000:
        break
    arr.append(next_num)
    print(arr)

for x in arr:
    if x % 2 == 0:
        result = result + x
print(result)
