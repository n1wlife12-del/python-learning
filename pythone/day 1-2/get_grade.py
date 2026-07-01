def get_grade(score):
    if score >= 90:
        return("Это A!")
    elif score >= 80 and score <= 89:
        return("Это B!")
    elif score >= 70 and score <= 79:
        return("Это C!")
    elif score >= 60 and score <= 69:
        return("Это D!")
    else:
        return("это f! :(")
score = int(input("Введите ваш балл: "))
grade = get_grade(score)
print(grade)    