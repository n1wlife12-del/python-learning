def rectangle_area(width, height):
    return width * height
width = float(input("Введите ширину:"))
height = float(input("Введите длинну: "))
print(f"Площадь прямоугольника равна {rectangle_area(width, height)}")