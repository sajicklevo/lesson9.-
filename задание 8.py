import json
import csv


def json_to_csv(json_file, csv_file):
    with open(json_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    with open(csv_file, 'w', newline='', encoding='UTF-8') as w_file:
        names = ['name', 'birthday', 'height', 'weight', 'car', 'languages']
        file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\n', fieldnames=names)
        file_writer.writeheader()
        for i in data:
            file_writer.writerow(i)


def read_json(json_file):
    with open(json_file, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in data:
            print(i)


def read_csv(csv_file):
    with open(csv_file, 'r', encoding='UTF-8') as file:
        reader = csv.reader(file)
        for i in reader:
            print(i)


def add_to_json(json_file):
    name = str(input('Введите имя сотрудника: '))
    birthday = int(input('Введите дату рождения сотрудника: '))
    height = int(input('Введите рост сотрудника: '))
    weight = int(input('Введите вес сотрудника: '))
    car = str(input('Введите true или false: '))
    languages = str(input('Введите язык программирования: ')).split(',')

    add_employee = {
        'name': name,
        'birthday': birthday,
        'height': height,
        'weight': weight,
        'car': car,
        'languages': languages
    }
    with open(json_file, 'r+', encoding='UTF-8') as file:
        data = json.load(file)
        data.append(add_employee)
        file.seek(0)
        json.dump(data, file, indent=4)


def add_to_csv(csv_file):
    name = str(input('Введите имя сотрудника: '))
    birthday = int(input('Введите дату рождения сотрудника: '))
    height = int(input('Введите рост сотрудника: '))
    weight = int(input('Введите вес сотрудника: '))
    car = str(input('Введите true или false: '))
    languages = str(input('Введите язык программирования: ')).split(',')

    add_employee = {'name': name, 'birthday': birthday, 'weight': weight, 'car': car, 'languages': languages}

    with open(csv_file, 'a', encoding="UTF-8", newline='') as w_file:
        names = ['name', 'birthday', 'weight', 'car', 'languages']
        file_writer = csv.DictWriter(w_file, delimiter=',', lineterminator='\n', fieldnames=names)

        if w_file.tell() == 0:
            file_writer.writeheader()

        file_writer.writerow(add_employee)


def read_info(json_file):
    name=str(input())
    with open(json_file,'r',encoding='UTF-8')as file:
        data=json.load(file)
    for person in data:
        if person['name'] == name:
            return person

def filter_by_languages(json_file):
    languages=str(input())
    lang=[]
    with open(json_file,'r',encoding='UTF-8')as file:
        data=json.load(file)
    for person in data:
        if languages['languages']:
            lang.append(person)
    return lang

def filter_by_year(json_file):
    year =str(input())
    total_height=0
    a=0
    with open(json_file,'r',encoding='UTF-8') as file:
        data=json.load(file)
    for person in data:
        if int(person['birthday'].split('.')[-1]<int(year)):
            total_height+=person['height']
            a+=1
    return total_height/a


while True:
    print('\nМеню:')
    print('1. Прочитать данные и преобразовать в JSON')
    print('2. Сохранить данные в CSV')
    print('3. Добавить нового сотрудника в JSON')
    print('4. Добавить нового сотрудника в CSV')
    print('5. Прочитать информацию о сотруднике по имени')
    print('6. Фильтрация по году рождения')
    print('7. Фильтрация по языку программирования')
    print('8. Выход')

    choice = input('Выберите действие: ')

    if choice == "1":
        read_json('json_file.json')

    elif choice == "2":
        read_csv('csv_file.csv')

    elif choice == "3":
        add_to_json('json_file.json')

    elif choice == "4":
        add_to_csv('csv_file.csv')

    elif choice == "5":
        print(read_info('json_file.json'))

    elif choice == "6":
        print(filter_by_year('json_file.json'))

    elif choice == "7":
        print(filter_by_languages('json_file.json'))

    else:
        break


