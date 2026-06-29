def convert(dollars, curs):
    return dollars * curs
curs = float(input("Какой курс рубля к доллару?:"))
dollars = float(input("Введите сумму в $: "))
rubles = convert(dollars, curs)
print(f"{dollars}$ по вашему курсу равен {rubles} рублей")
    