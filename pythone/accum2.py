word = input("Word: ")
let = ""
for letter in word:
    if letter not in "aeiou":
        let += letter
print(let)