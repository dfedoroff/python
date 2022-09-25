# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip,
# enumerate, list comprehension. Продолжение, Семинар 6, hw6-5
#
# -----------------
# Задача 5:
# Напишите программу, удаляющую из текста все слова, содержащие "АБВ".

def rem_words(text):
    text = list(filter(lambda i: 'АБВ' not in i, raw_text.split()))
    return " ".join(text)

raw_text = 'Напишите прогрАБВмму, удАБВбвляющую из текстАБВ все словАБВ, содержАБВщие "АБВ"'
print(f'Изначальный текст: {raw_text}')
print(f'Итоговый результат: {rem_words(raw_text)}')
