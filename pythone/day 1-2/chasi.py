def convert(hour):
    return hour * 60
hour = int(input("Введите кол часов: "))
result = convert(hour)
print(f"{hour} часа(ов) это {result} минут")
