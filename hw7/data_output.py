def print_data(file_name):
    with open(file_name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            line = line.replace(';', '\t')
            print(line)
