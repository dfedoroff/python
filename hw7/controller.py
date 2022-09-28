import data_input
import data_output
import user_interface as ui

def start():
    welcome_msg = 'Телефонный справочник с импортом и экспортом данных в нескольких форматах'
    print(welcome_msg)
    while True:
        choice = ui.choose_menu()
        if choice == '1':
            data = data_input.input_data()
            print(*data, '\n')
            data_input.write_in_row(data)
            data_input.write_in_column(data)
        elif choice == '2':
            data_output.print_data('data_row.csv')
        elif choice == '3':
            data_output.print_data('data_col.csv')
        elif choice == '4':
            break
