x = "fdadfafd"
y = len(x)
print("x的长度是", y)

if y % 2 == 0:
    print("能被2整除")
    if y % 3 == 0:
        print("能被3整除")
    elif y % 4 == 0:
        pass
else:
    print("哈哈")

# 终止