def filter_students_by_grade(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split()
            name = ' '.join(data[:-1])
            grade = int(data[-1])
            if grade < 3:
                print(name)

filter_students_by_grade('grades.txt')
