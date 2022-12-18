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
    print(data_from_serch)
    return data_from_serch

# def search_data_from_list(all_data: list, need_find_data: list) -> list:

#     data_from_serch = []

#     for count in range(0, len(all_data), 1):
#         if [all_data[count][0]].count(need_find_data[0]) or\
#                 [all_data[count][1]].count(need_find_data[1]) or\
#                 [all_data[count][2]].count(need_find_data[2]) or\
#                     [all_data[count][3]].count(need_find_data[3]):
#                     data_from_serch.append(all_data[count])
#     print(data_from_serch)
#     return data_from_serch
