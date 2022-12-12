def print_all_list_in_terminal(print_data):
    
    print("\n")
    print("\t {} \t {} \t {} \t {} \t {}\n".format("№","Фамилия","Имя","Отчество","Телефон"))
    print("\t-------------------------------------------------------------")
    
    for count in range(0, len(print_data), 1):
        print("\t {} \t {} \t {} \t {} \t {}\n".format(count+1, print_data[count][0], \
            print_data[count][1], print_data[count][2], print_data[count][3]))

#old_data = [["Фамилию", "Имя", "Отчество", 8900000000], ["Фамилию", "Имя", "Отчество", 8900000000]]
#print_all_list_in_terminal(old_data)