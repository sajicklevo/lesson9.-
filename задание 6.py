def get_sum_of_numbers(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
        numbers_list = [int(num) for num in content.split() if num.isdigit()]
        sum_of_numbers = sum(numbers_list)

    return sum_of_numbers


file_name = 'text.txt'
result = get_sum_of_numbers(file_name)
print(result)