from pytube import YouTube

def download():
    yt = YouTube(str(input('Вставьте YouTube ссылку: ')))
    video = yt.streams.filter(file_extension='mp4').order_by('resolution')
    s = 1
    for n in video:
        print(f'{str(s)}. {str(n)}')
        s += 1
    num = int(input('Выберите номер видео: '))
    file = video[num - 1]
    path = str(input('Нажмите Enter для сохранения файла в текущей папке или укажите иной адрес: '))
    file.download(path)
    print('Загрузка завершена!')
