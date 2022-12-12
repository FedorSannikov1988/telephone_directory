from pathlib import Path
import print_data
'''
импортировал import print_data для 
того что бы проверять что беру из файла
'''

'''
Тяжеловесно конешно но зато я смог написать очень быстро 
данный модуль хотя конешно применение такого 
количесва for (особенно в модуле loading_data_from_phone_directory())
не оправдано (можно куда изящнее)
'''

file_name = "phone_directory.csv"
relative_file_directory = Path(file_name)


def safe_data_in_phone_directory(data_for_write: list, flag_for_format_safe_data: str="line"):

    global relative_file_directory

    with open(relative_file_directory, 'w', encoding='utf-8') as data:
        
        match flag_for_format_safe_data:
            case "column": data.write("column\n")
            case "line": data.write("line\n")

        for count in range(0, len(data_for_write), 1):
            if flag_for_format_safe_data == "column":
                data.write("{}\n\n{}\n\n{}\n\n{}\n\n".format(data_for_write[count][0], \
                    data_for_write[count][1], data_for_write[count][2], data_for_write[count][3]))
            elif flag_for_format_safe_data == "line":
                data.write("{};{};{};{}\n".format(data_for_write[count][0], \
                    data_for_write[count][1], data_for_write[count][2], data_for_write[count][3]))


def loading_data_from_phone_directory() -> list:

    global relative_file_directory

    with open(relative_file_directory, 'r', encoding='utf-8') as data_from_file:
        
        data_for_pars = list()        
        
        for line in data_from_file:
            data_for_pars.append(line)     

        for count in range(0, len(data_for_pars), 1):
            data_for_pars[count] = data_for_pars[count].replace('\n', '')
        
        flag_for_format_safe_data = str(data_for_pars[0])
        data_for_pars.pop(0)

        if flag_for_format_safe_data == "line":
            resalt_data = list()
            for count in range(0, len(data_for_pars), 1):
                resalt_data.append(data_for_pars[count].split(";"))
            return resalt_data

        elif flag_for_format_safe_data == "column":
            sorted_data = list()
            for count in range(0, len(data_for_pars), 1):
                if data_for_pars[count] != "" and not data_for_pars[count].isdigit():
                    sorted_data.append(data_for_pars[count])
                if data_for_pars[count] != "" and data_for_pars[count].isdigit():
                    sorted_data.append(int(data_for_pars[count]))
            
            resalt_data = list()
            count_for_element = 0
            for _ in range(0, int(len(sorted_data)/4), 1):
                resalt_data.append([sorted_data[0+count_for_element],\
                    sorted_data[1+count_for_element],\
                        sorted_data[2+count_for_element],\
                            sorted_data[3+count_for_element]])
                count_for_element +=4
            return resalt_data

'''
это для проверки работоспособности кода:
'''

'''
data_for_write = [["Фамилия1", "Имя1*", "Отчество1", 89609752504], ["Фамилия2", "Имя2*", "Отчество2", 89609752504], ["Фамилию3", "Имя3*", "Отчество3", 89609752504]]
#flag = "line"
flag = "column"
safe_data_in_phone_directory(data_for_write, flag)
data = loading_data_from_phone_directory()
print_data.print_all_list_in_terminal(data)
'''