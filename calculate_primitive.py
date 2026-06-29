def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/" and b !=0:
        return a / b
    elif operation == "/" and b == 0:
        return "Делить на ноль нельзя"
    
a = float(input("Первое число: "))
b = float(input("Второе число: "))
operation = input("Операция (+, -, *, /): ")
result = calculate(a, b, operation)
print(f"Результат: {result}")