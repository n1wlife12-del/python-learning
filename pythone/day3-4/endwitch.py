file = input("Введите название файла с форматом .: ").strip().lower()
if file.endswith(".jpg") or file.endswith(".png"):
    print(f"{file} - Это Картинка!")
elif file.endswith(".txt"):
    print(f"{file} - Это текстовый файл")
elif file.endswith(".mp3"):
    print(f"{file} - Это музыка!")
elif file.endswith(".mov") or file.endswith(".mp4"):
    print(f"{file} - Это видео!")
else:
    print(f"{file} - не поддерживаемый формат файла:(")

