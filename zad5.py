def calculate_total(price, quantity, discount):
    return price * quantity - discount


price = float(input("Введите цену: "))
quantity = int(input("Введите кол-во: "))
discount = float(input("Введите скидку (сумма): "))

result = calculate_total(price, quantity, discount)
print(f"Итого: {result}")