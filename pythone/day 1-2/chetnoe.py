def is_even(num):
    return num % 2 == 0
num =float(input("Введите число: "))
if is_even(num):
    print("Чётное")
else:
    print("Нечетное")