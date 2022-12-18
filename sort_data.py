import validation
import logger

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

    ind_list_sort = validation.validation_answer_number(1, 4)
    
    match ind_list_sort:
        case 1: logger.log_entry("фамилии")
        case 2: logger.log_entry("имени")
        case 3: logger.log_entry("отчеству") 
        case 4: logger.log_entry("номеру телефона") 

    print("\n")
    print("\t\t ВОЗРАСТАНИЮ ИЛИ УБЫВАНИЮ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  убывание")
    print("\t 2 -  возрастание")
    print("\n")

    order_sort = validation.validation_answer_number(1, 2)

    match order_sort:
        case 1: logger.log_entry("убывание")
        case 2: logger.log_entry("возрастание")
    
    if order_sort == 1:
        flag_sort_order = False
    else:
        flag_sort_order = True
        
    data_result = sorted(data, key = lambda el: el[ind_list_sort-1], reverse = flag_sort_order)

    return data_result