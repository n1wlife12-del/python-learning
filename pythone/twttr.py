word = input("Word: ")
let = ""
for letter in word:
    if letter.lower() not in "aeiou":
        let += letter
print(let)
