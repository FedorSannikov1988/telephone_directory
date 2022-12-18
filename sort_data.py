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
