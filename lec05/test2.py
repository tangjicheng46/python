# n = 12345

# 第一次：
# r = n % 10 = 5
# n = n // 10 = 1234
# l = [5]

# 第二次：
# r = n % 10 = 4
# n = n // 10 = 123
# l = [5, 4]

# 第三次：
# r = n % 10 = 3
# n = n // 10 = 12
# l = [5, 4, 3]

# 第四次：
# r = n % 10 = 2
# n = n // 10 = 1

# 第五次：
# r = n % 10 = 1
# n = n // 10 = 0
# 终止

# n = n // 10 = 0

# l = [5, 4, 3, 2, 1]
# l = [5, 4, 3, 4, 5]
# l = [5, 4, 3, 3, 4, 5]
# 数组array，列表list

def isPalindrome(n):
    if n < 0:
        return False
    l = []
    # 算术方法，取整数的每一位
    while n > 0:
        r = n % 10 
        n = n // 10
        l.append(r)

    i = 0
    while i < (len(l) // 2):
        if l[i] != l[len(l) - 1 - i]:
            return False
        i += 1
    return True

def isPalindrome2(n):
    if n < 0:
        return False
    s = str(n)

    i = 0
    while i < (len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
        i += 1
    return True

print(isPalindrome(12321))
print(isPalindrome(12345))


# 12321 --->  "12321"
print(isPalindrome2(12321))
print(isPalindrome2(12345))