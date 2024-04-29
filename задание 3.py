from collections import Counter

def most_common_word(line):
    words = line.split()
    word_counts = Counter(words)
    most_common = word_counts.most_common(1)[0][0]
    return most_common

with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    result = most_common_word(line)
    print(result)
