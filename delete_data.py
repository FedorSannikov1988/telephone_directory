import print_data

def delet_data_from_list(data: list):
    
    print("\n")
    print("\t ПРОЦЕДУРА УДАЛЕНИЯ ДАННЫХ:")
    print("\t---------------------------")
    
    while True:
        text = "\tВведите через пробел номера строк \nкоторые необходимо удалить после чего нажмите 'Enter'\n"
        human_answer_string = input(f"{text}")
        try:
            human_answer_namber = list(map(int, list(human_answer_string.split())))
            break
        except ValueError:
            print("Повторите ввод")
            continue
    
    function = lambda x: x <= len(data)
    human_answer_namber = list(filter(function, human_answer_namber))
    #print(human_answer_namber)

    data_out = []
    
    for count in range(0, len(data), 1):
        if human_answer_namber.count(int(count+1)) == 0:
            data_out.append(data[count]) 
    
    return data_out

'''
data = [["Фамилию", "Имя", "Отчество", 8900000000], ["Фамилию", "Имя", "Отчество", 8900000000], ["Фамилию", "Имя", "Отчество", 8900000000], ["Фамилию", "Имя", "Отчество", 8900000000]]

print_data.print_all_list_in_terminal(data)

data1 = delet_data_from_list(data)

print_data.print_all_list_in_terminal(data1)
'''