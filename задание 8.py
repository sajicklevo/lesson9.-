import json
import csv

def read_json(json_file_path):
    with open(json_file_path,'r',encoding='UTF-8') as file:
        data=json.load(file)
        for row in data:
            print(row)
json_file_path = '/home/danila/Загрузки/employees.json'
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)


def write_csv(data, json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    with open('/home/danila/Загрузки/employees.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        header = list(data[0].keys())
        csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row.values())



def add_new_employee(file_path):
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    new_employee = {}
    new_employee['name'] = input('Введите имя сотрудника: ')
    new_employee['hb'] = input('Введите дату рождения сотрудника: ')
    new_employee['position'] = input('Введите язык программирования сотрудника: ')
    data.append(new_employee)
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=2)


def add_new_employee_to_csv(csv_file_path):
    new_employee = {}
    new_employee['name'] = input('Введите имя сотрудника: ')
    new_employee['dob'] = input('Введите дату рождения сотрудника: ')
    new_employee['position'] = input('Введите язык программирования сотрудника: ')
    fieldnames = ['name', 'dob', 'position']
    with open(csv_file_path, 'a', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow(new_employee)


def search_employee_by_name(csv_file_path, search_name):
    with open(csv_file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        found = False
        for row in reader:
            if row['name'] == search_name:
                found = True
                print(f"Информация о сотруднике по имени '{search_name}':")
                print(f"Имя: {row['name']}")
                print(f"Дата рождения: {row['dob']}")
                print(f"Должность: {row['position']}")
        if not found:
            print(f"Сотрудник с именем '{search_name}' не найден.")


def filter_employees_by_language(csv_file_path, programming_language):
    with open(csv_file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        filtered_employees = []
        for row in reader:
            if programming_language.lower() in row['languages'].lower():
                filtered_employees.append(row)

        if filtered_employees:
            print(f"Список сотрудников владеющих языком программирования '{programming_language}':")
            for employee in filtered_employees:
                print(f"Имя: {employee['name']}, Должность: {employee['position']}")
        else:
            print(f"Нет сотрудников, владеющих языком программирования '{programming_language}'.")


def filter_employees_by_birth_year(csv_file_path, target_birth_year):
    with open(csv_file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        total_height = 0
        num_employees = 0
        for row in reader:
            if int(row['birth_year']) < target_birth_year:
                total_height += float(row['height'])
                num_employees += 1

        if num_employees > 0:
            average_height = total_height / num_employees
            print(
                f"Средний рост всех сотрудников, у которых год рождения меньше {target_birth_year}: {average_height:.2f} см")
        else:
            print(f"Нет данных о сотрудниках с годом рождения меньше {target_birth_year}.")


def main_menu():
    csv_file_path = '/home/danila/Загрузки/employees.csv'
    while True:
        print("\nВыберите действие:")
        print("1. Фильтрация сотрудников по языку программирования")
        print("2. Фильтрация среднего роста по году рождения")
        print("3. Выход из программы")
        choice = input("Введите номер действия: ")

        if choice == '1':
            programming_language = input("Введите язык программирования для фильтрации: ")
            filter_employees(csv_file_path, 'languages', programming_language)

        elif choice == '2':
            target_birth_year = int(input("Введите год рождения для фильтрации: "))
            filter_employees(csv_file_path, 'birth_year', target_birth_year)

        elif choice == '3':
            print("Программа завершена.")
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")


def filter_employees(csv_file_path, field_name, search_value):
    with open(csv_file_path, mode='r') as csv_file:
        reader = csv.DictReader(csv_file)
        filtered_employees = []
        for row in reader:
            if field_name in row and row[field_name] == str(search_value):
                filtered_employees.append(row)

        if filtered_employees:
            if field_name == 'languages':
                print(f"Список сотрудников владеющих языком программирования '{search_value}':")
            elif field_name == 'birth_year':
                print(
                    f"Средний рост всех сотрудников, у которых год рождения меньше {search_value}: {calculate_average_height(filtered_employees):.2f} см")

            for employee in filtered_employees:
                print(f"Имя: {employee['name']}, Должность: {employee['position']}")

        else:
            if field_name == 'languages':
                print(f"Нет сотрудников, владеющих языком программирования '{search_value}'.")
            elif field_name == 'birth_year':
                print(f"Нет данных о сотрудниках с годом рождения меньше {search_value}.")


def calculate_average_height(employees):
    total_height = 0
    num_employees = len(employees)
    for employee in employees:
        total_height += float(employee['height'])

    return total_height / num_employees

if __name__ == "__main__":
    main_menu()
