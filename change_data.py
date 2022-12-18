import add_data

def change_data_in_telephone_directory(data: list, data_from_search: list) -> list:

    print("\n")
    print("\t ПРОЦЕДУРА ИЗМЕНЕНИЯ ДАННЫХ:")
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

    # элемент, который надо изменить из поиска и его индекс в справочнике
    change_element.append(data_from_search[human_answer_namber-1])
    for i in data:
        if i == change_element[0]:
            index_changing_element = data.index(i)

    for i in range(0, len(data)):
        if i == index_changing_element:
            for i in range(0, len(need_change_data)):
                if need_change_data[i] != '' : change_element[0][i] = need_change_data[i]
                else: i +=1
    return data


# data = [["11", "11", "11", 123], ["22", "22", "22", 123],["33", "33", "33", 123], ["11", "41", "41", 123], ["11", "55", "5", 123]]

# data_from_search = [["11", "11", "11", 123], ["11", "41", "41", 123], ["11", "55", "5", 123]]

# change_element = []

# need_change_data = add_data.input_data_in_phone_directory()
# human_answer_namber = 2

#         # элемент, который надо изменить и его индекс
# change_element.append(data_from_search[human_answer_namber-1])
# index_changing_element = human_answer_namber - 1

# #индекс элемента который надо изменить в общем справочнике
# for i in data:
#     if i == change_element[0]:
#         index_changing_element_in_data = data.index(i)

# print(f'индекс в дата {data.index(i)}')


# for i in range(0, len(data_from_search)):
#     if i == index_changing_element:
#         for i in range(0, len(need_change_data)):
#             if need_change_data[i] != '' : change_element[0][i] = need_change_data[i]
#             else: i +=1

# print(change_element) 
# print(data)
# print(data_from_search)

