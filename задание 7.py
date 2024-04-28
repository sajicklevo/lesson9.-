import random
def substitution_cipher(text):
    a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    b = list(a)
    random.shuffle(b)

    mapping = dict(zip(list(a), b))

    result = ''
    for char in text:
        if char.isalpha():
            upper_char = char.upper()
            substituted_char = mapping.get(upper_char, upper_char)
            result += substituted_char if char.isupper() else substituted_char.lower()
        else:
            result += char
    return result


with open('input.txt', 'r') as file:
    lines = file.readlines()

output_lines = []
for line in lines:
    encrypted_line = substitution_cipher(line.strip())
    output_lines.append(encrypted_line)

with open('output.txt', 'w') as file:
    for encrypted_line in output_lines:
        file.write(encrypted_line + '\n')

