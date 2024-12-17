import os

# Указываем путь к директории с исходными файлами
folder_path = r"C:\Users\Dell\Desktop\Учеба\открытие и чтение\py-homework-basic-files\2.4.files\sorted"

# Получаем список всех файлов в папке
files = os.listdir(folder_path)

# Создаем список для хранения данных файлов и их количества строк
file_data = []

# Проходим по каждому файлу в папке
for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    # Проверяем, является ли элемент файлом
    if os.path.isfile(file_path):
        # Открываем файл и считаем количество строк
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file_data.append((file_name, len(lines), lines))

# Сортируем список файлов по количеству строк
file_data.sort(key=lambda x: x[1])

# Создаем результатирующий файл для записи
output_file_path = os.path.join(folder_path, 'merged_sorted.txt')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # Проходим по отсортированным данным и записываем в новый файл
    for file_name, line_count, lines in file_data:
        # Записываем служебную информацию: имя файла и количество строк
        output_file.write(f"{file_name}\n{line_count}\n")
        # Записываем содержимое файла
        output_file.writelines(lines)

print(f"Результирующий файл создан: {output_file_path}")