import print_data



def search_data_from_list(data: list):

    print("\n")
    print("\t ПРОЦЕДУРА ПОИСКА ДАННЫХ:")
    print("\t---------------------------")
    
    text = " \nПОИСК:\n"
    human_answer_string = input(f"{text}")

    data_from_serch = []

    for el in data:
        if human_answer_string in el:
            data_from_serch.append(el)
 
    if data_from_serch == []: print('Совпадений не найдено!')
    else: print(print_data.print_all_list_in_terminal(data_from_serch))

    return data_from_serch