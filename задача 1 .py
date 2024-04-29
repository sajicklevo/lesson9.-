import os

os_name = os.name
print('Имя операционной системы:', os_name)

path = os.getcwd()
print('Путь до папки:', path)

extensions = set()
while True:
    extension = input('Введите расширение файла (или "exit" для завершения): ')
    if extension == 'exit':
        break
    else:
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
                    print(f'Файл {file_name} был перемещен в папку {folder_name}')

    for folder_name in os.listdir(path):
        folder_path = os.path.join(path, folder_name)
        if os.path.isdir(folder_path):
            num_files = sum(not os.path.isdir(os.path.join(folder_path, j)) for j in os.listdir(folder_path))
            total_size = sum(os.path.getsize(os.path.join(folder_path, j)) for j in os.listdir(folder_path)) / (1024 * 1024 * 1024)
            print(f'В папке {folder_name} перемещено {num_files} файлов, их суммарный размер {total_size:.2f} гигабайта')

            for file_name in os.listdir(folder_path):
                file_path = os.path.join(folder_path, file_name)
                if os.path.isfile(file_path):
                    new_file_name = 'new_' + file_name
                    new_file_path = os.path.join(folder_path, new_file_name)
                    os.rename(file_path, new_file_path)
                    print(f'Файл {file_name} был переименован в {new_file_name}')

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))
