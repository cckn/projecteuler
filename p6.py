sum1 = 0
sum2 = 0

for x in range(1, 101):
    sum1 += x ** 2
    sum2 += x

sum2 = sum2 ** 2

print(sum1)
print(sum2)

print(sum2 - sum1)
