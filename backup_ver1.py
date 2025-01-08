import os
import time
import zipfile

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\Users\\SOGAZ-Med\\Pictures\\цель']

# 2. Прописываем путь, куда будем копировать наши файлы.
target_dir = 'C:\\Users\\SOGAZ-Med\\Pictures\\Копия'

# Создаем целевую директорию, если она не существует
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 3. Создаем имя для zip-архива с текущими датой и временем.
target = os.path.join(target_dir, time.strftime('%Y%m%d%H%M%S') + '.zip')

# 4. Используем zipfile для создания zip-архива
try:
    with zipfile.ZipFile(target, 'w') as zipf:
        for folder in source:
            for root, _, files in os.walk(folder):
                for file in files:
                    file_path = os.path.join(root, file)  # Полный путь к файлу
                    # Добавляем файл в архив, используя относительный путь
                    zipf.write(file_path, os.path.relpath(file_path, start=os.path.dirname(folder)))  
    print('Резервная копия успешно создана в', target)
except Exception as e:
    print('Создание резервной копии НЕ УДАЛОСЬ:', e)  # Выводим текст ошибки





