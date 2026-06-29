def greet_by_time(hour):
    if hour >= 6 and hour <= 11:
        return "Доброе утро"
    elif hour >= 12 and hour <= 17:
        return "Добрый день"
    elif hour >= 18 and hour <= 21:
        return "Добрый вечер"
    else:
        return "Доброй ночи"
hour = int(input("Введите час (0-23):"))
greeting = greet_by_time(hour)
print(greeting)    