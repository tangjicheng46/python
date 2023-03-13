# 阶乘
# n! = 1*2*...*n 
n = 10 
i = 1
result = 1
while i <= n:
    result = result * i 
    i = i + 1
    if i == 3:
        continue
        # break
print(result)