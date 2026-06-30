def dig_to_word(n):
    if n == 0:
        return "ноль"
    elif n == 1:
        return "один"
    elif n == 2:
        return "два"
    elif n == 3:
        return "три"
    elif n == 4:
        return "четыре"
    elif n == 5:
        return "пять"
    elif n == 6:
        return "шесть"
    elif n == 7:
        return "семь"
    elif n == 8:
        return "восемь"
    elif n == 9:
        return "девять"
    else:
        return "Нету в базе"
n = int(input("Введите число от 0 до 9: "))
result = dig_to_word(n)
print(f"{n} - {result}")
