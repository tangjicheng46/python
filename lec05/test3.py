def lengthOfLastWord(s):
    i = len(s) - 1
    while i >= 0 and s[i] == " ":
        i -= 1
    j = i 
    while j >= 0 and s[j] != " ":
        j -= 1
    return i - j


s = "   fly me   to   the moon      "
# [3, 2, 2, 3, 4]

def lengthOfFirstWord(s):
    i = 0
    while i <= len(s) - 1 and s[i] == " ":
        i += 1
    j = i 
    while j <= len(s) - 1 and s[j] != " ":
        j += 1
    return j - i

def f(s):
    return len(s.split(" ")[-1])

print(lengthOfFirstWord(s))

# print(lengthOfLastWord(s))