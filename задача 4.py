def censor_text(file_name):
    with open('stop_words.txt', 'r') as stop_file:
        stop_words = stop_file.read().lower().split()
    with open(file_name, 'r') as text_file:
        text = text_file.read().lower()
        for word in stop_words:
            text = text.replace(word, '*' * len(word))
    print(text)

censor_text('input.txt')