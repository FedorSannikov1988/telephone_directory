import add_data

def change_data_in_telephone_directory(data: list, data_from_search: list) -> list:

    print("\n")
    print("\tПРОЦЕДУРА ИЗМЕНЕНИЯ ДАННЫХ:")
    print("\t---------------------------")
    
    while True:
        text = "\tВведите номер строки \nкоторую необходимо изменить после чего нажмите 'Enter'\n"
        
        human_answer_string = input(f"{text}")

        if not human_answer_string.isdigit():
            print("Повторите ввод")
            continue
        try:
            human_answer_namber = int(human_answer_string)
            break
        except ValueError:
            print("Повторите ввод")
            continue

    change_element = []

    need_change_data = add_data.input_data_in_phone_directory()

    change_element.append(data_from_search[human_answer_namber-1])

    for i in data:
        if i == change_element[0]:
            index_changing_element = data.index(i)

    for i in range(0, len(data)):
        if i == index_changing_element:
            for i in range(0, len(need_change_data)):
                if need_change_data[i] != '': change_element[0][i] = need_change_data[i]
                else: i +=1
		
    return data
