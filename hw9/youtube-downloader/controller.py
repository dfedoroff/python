import audio
import video
import user_interface as ui

def start():
    welcome_msg = 'Загрузчик видео и аудио с YouTube'
    print(welcome_msg)
    while True:
        choice = ui.select_item()
        if choice == '1':
            video.download()
        elif choice == '2':
             audio.download()
        elif choice == '3':
            break
