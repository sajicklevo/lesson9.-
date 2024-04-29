import os
import random
import string

osname = os.name
print('Имя вашей операционной системы:', osname)

path = os.getcwd()
print('Путь до папки:', path)

extensions = set()
while True:
    extension = input('Введите расширение файла (или введите "exit" для завершения): ')
    if extension == 'exit':
        break
    extensions.add(extension)
print('Расширения файлов:', extensions)

for file_name in os.listdir(path):
    if os.path.isfile(os.path.join(path, file_name)):
        file_extension = file_name.split('.')[-1]
        if file_extension in extensions:
            folder_name = file_extension.upper()
            if not os.path.exists(os.path.join(path, folder_name)):
                os.makedirs(os.path.join(path, folder_name))
            new_file_path = os.path.join(path, folder_name, file_name)
            os.rename(os.path.join(path, file_name), new_file_path)
print('Файлы были перемещены в папки с соответствующими расширениями')

for ext in os.listdir(path):
    if os.path.isdir(os.path.join(path, ext)):
        files_moved = len(os.listdir(os.path.join(path, ext)))
        total_size = sum(os.path.getsize(os.path.join(path, ext, file)) for file in os.listdir(os.path.join(path, ext)))
        print(f'В папке с файлами {ext} перемещено {files_moved} файлов, их суммарный размер - {total_size} байт')

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
