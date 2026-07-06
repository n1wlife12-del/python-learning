gor = input("Введите название города: ").strip().lower()
if gor == "москва" or gor == "moscow":
    print(f"{gor} - Столица России")
elif gor == "минск" or gor == "minsk":
    print(f"{gor} - Столица Беларуси")
elif gor == "астана" or gor == "astana":
    print(f"{gor} - Столица КЗ")
else:
    print(f"{gor} - Не знаю такую столицу")