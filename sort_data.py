import validation

def sorting_data(data: list):

    
    print("\n")
    print("\t\t   СОРТИРОВАТЬ ЗАПИСИ ПО")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  фамилии")
    print("\t 2 -  имени")
    print("\t 3 -  отчеству")
    print("\t 4 -  номеру телефона")
    print("\n")

    validation.validation_answer_number(1, 4)

    print("\n")
    print("\t\t ВОЗРАСТАНИЮ ИЛИ УБЫВАНИЮ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  убывание")
    print("\t 2 -  возрастание")
    print("\n")

    if validation.validation_answer_number(1, 2) == 1:
        flag_sort_order = False
    else:
        flag_sort_order = True

    data_result = sorted(data, key = lambda el: el[0], reverse=flag_sort_order)

    return data_result



# data = [["Фамилия1", "Имя1", "Отчество1", 123], ["qw", "Имя1", "r", 123], ["Амилия3", "Имя2", "Отчество2", 123], \
#     ["Фамилию3", "Имя3", "Отчество3", 123], ["qwe", "Имя5", "rr", 236], ["Фамилия1", "Имя1", "Отчество1", 123], \
#         ["Фамилию5", "Имя5", "Отчество5", 123], ["Фамилию6", "Имя6", "Отчество6", 123], ["qw45", "Имя1", "r", 16623], ["awe78", "Имя5", "rr", 23556]]

# sorted(data)
# print(sorted(data, key = lambda el: el[3], reverse=True))

