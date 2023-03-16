# s = "XVII"
def romanToInt(s):
    result = 0
    d = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M":1000}
    i = 0
    while i < len(s):
        j = len(s) - 1 - i
        before = j - 1
        if before >= 0 and s[j] == "V" and s[before] == "I":
            result += 4
            i += 2
        elif before >= 0 and s[j] == "X" and s[before] == "I":
            result += 9
            i += 2
        elif before >= 0 and s[j] == "L" and s[before] == "X":
            result += 40
            i += 2
        elif before >= 0 and s[j] == "C" and s[before] == "X":
            result += 90
            i += 2
        elif before >= 0 and s[j] == "D" and s[before] == "C":
            result += 400
            i += 2
        elif before >= 0 and s[j] == "M" and s[before] == "C":
            result += 900
            i += 2
        else:
            result += d[s[j]]
            i += 1
    return result

# s = "XVII"
# 1 + 1 + 5 + 10

# 10 + 5 + 1 + 1
# for element in s:
# s[0] s[1] s[2] s[3]



# 加法有交换律
# 1 + 2 + 3 + 4
# 4 + 3 + 2 + 1

# def romanToInt2(s):
#     result = 0
#     d = {"I":1, "V": 5, "X": 10, "L": 50, "C": 100, "D":500, "M":1000}
#     for element in s:
#         result += d[element]
#     return result

# 第0次迭代： s[2] , s[len(s) - 1 - 0(i)] = s[3 - 1]
# 第1次迭代： s[1] , s[len(s) - 1 - 1(i)]
# 第2次迭代： s[0] , s[len(s) - 1 - 2(i)]
print(romanToInt("III"))

        # before = cur - 1

