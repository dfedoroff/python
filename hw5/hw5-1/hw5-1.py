# Ускоренная обработка данных: lambda, filter, map, zip, enumerate,
# list comprehension. Семинар 5, hw5-1
#
# -----------------
# Задача 1:
# Напишите программу, удаляющую из текста все слова, содержащие "АБВ".

def read_file(file):
    with open(file, 'r', encoding='utf-8') as data:
        raw_text = data.read()
    return raw_text

def rem_words(text):
    text = list(filter(lambda x: 'АБВ' not in x, text.split()))
    return " ".join(text)

print(f'Изначальный текст: {read_file("input-data.txt")}')
text = rem_words(read_file('input-data.txt'))
print(f'Итоговый результат: {text}')