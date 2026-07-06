word = input("camelCase: ")
result = ""
flag = False
for letter in word:
    if letter == "_":
        flag = True
    else:
        if flag:
            result += letter.upper()
            flag = False
        else:
            result += letter
print(result)
