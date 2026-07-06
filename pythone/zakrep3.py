def count_vowels(s):
    vowels = "ауоыиэяюёе"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


s = input("Введите строку: ")
result = count_vowels(s)
print(f"Гласных букв: {result}")
