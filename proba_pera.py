'''
data_for_write = [["Фамилия1", "Имя1*", "Отчество1", 89609752504], ["Фамилия2", "Имя2*", "Отчество2", 89609752504], ["Фамилию3", "Имя3*", "Отчество3", 89609752504]]
#flag = "line"
flag = "column"
safe_data_in_phone_directory(data_for_write, flag)
data = loading_data_from_phone_directory()
print_data.print_all_list_in_terminal(data)
'''

data_1 = [["Фамилия1", "Имя1", "Отчество1", 123], ["Фамилия1", "Имя1", "Отчество1", 123], ["Фамилию3", "Имя3", "Отчество3", 123]]

'''
data_2 = [["Фамилия1", "Имя1", "Отчество1", 123]]


print(data_1[0] == data_2[0])

print(data_1[0] == data_1[1])
'''

data_1 = [["Фамилия1", "Имя1", "Отчество1", 123], ["Фамилия2", "Имя2", "Отчество2", 123], \
    ["Фамилию3", "Имя3", "Отчество3", 123], ["Фамилия1", "Имя1", "Отчество1", 123], \
        ["Фамилию5", "Имя5", "Отчество5", 123],["Фамилию6", "Имя6", "Отчество6", 123]]

'''
data_2 = []

for count in data_1:
    if count not in data_2:
        data_2.append(count)
'''
data_2 = []

[data_2.append(x) for x in data_1 if x not in data_2]

data_3 = [element for index, element in enumerate(data_1) if element not in data_1[:index]]

print(data_1[:2])
print(data_3)