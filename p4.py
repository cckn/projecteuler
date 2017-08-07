
palindrome_arr = []


def is_palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False

for x in range(999, 1):
    for y in range(999, 1):
        num = x * y
        if is_palindrome(num):
            palindrome_arr.append(num)


# print(palindrome_arr)
print(max(palindrome_arr))
