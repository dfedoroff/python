from pytube import YouTube

def download():
    yt = YouTube(str(input('Вставьте YouTube ссылку: ')))
    audio = yt.streams.filter(only_audio=True).order_by('abr')
    s = 1
    for n in audio:
        print(f'{str(s)}. {str(n)}')
        s += 1
    num = int(input('Выберите номер аудио: '))
    file = audio[num - 1]
    path = str(input('Нажмите Enter для сохранения файла в текущей папке или укажите иной адрес: '))
    file.download(path)
    print('Загрузка завершена!')
