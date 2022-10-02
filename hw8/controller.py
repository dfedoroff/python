import data_input
import search_data
import user_interface as ui
import logger

def start():
    temp = ui.choose_menu()
    if temp == 1:
        print('Внесите в справочник новый контакт.')
        entry = data_input.record()
        logger.log_to_file(entry)
        logger.write_json(entry)
        start()
    if temp == 2:
        print('Поиск контакта в справочнике.')
        entry = search_data.search()
        logger.reading_file(entry)
        start()
    if temp == 3:
        print('Вывод на печать всех контактов.')
        logger.read_all_file()  
        start()
    if temp == 4:
        print('Работа cо справочником завершена.')
        exit
