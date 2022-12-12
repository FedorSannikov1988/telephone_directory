def choosing_start_work_action():

    print("\n")
    print("\t       ЗАПУЩЕН ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 - просмотреть все записи в справочнике")
    print("\t 2 - добавить запись в справочник")
    print("\t 3 - удалить запись из справочника")
    print("\t 4 - найти запись в справочнике")
    print("\t 5 - выйти из справочника")

    while True:
        human_answer_string = input(f"Какое действие выбираете: ")
        
        if not human_answer_string.isdigit() or int(human_answer_string) > 5 or int(human_answer_string) < 1 :
            print("Повторите ввод действия")
            continue

        try:
            human_answer_namber = int(human_answer_string)
            break
        except ValueError:
            print("Повторите ввод действия")
            continue
    
    return human_answer_namber

def choosing_action_for_safe():

    print("\n")
    print("\t     В КАКОМ ФОРМАТЕ СОХРАНИТЬ ДАННЫЕ")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 - в столбик")
    print("\t пример:")
    print("\t Фамилия1")
    print("\t Имя1")
    print("\t Отчество1")
    print("\t Телефон1")
    print("\t","-"*10)
    print("\t Фамилия2")
    print("\t Имя2")
    print("\t Отчество2")
    print("\t Телефон2")
    print("\t","-"*41)
    print("\t 2 - в сторочку")
    print("\t пример:")
    print("\t Фамилия1;Имя1;Отчество1;Телефон1")
    print("\t Фамилия2;Имя2;Отчество2;Телефон2")

    while True:
        human_answer_string = input(f"Какое действие выбираете: ")
        
        if not human_answer_string.isdigit() or int(human_answer_string) > 2 or int(human_answer_string) < 1 :
            print("Повторите ввод действия")
            continue

        try:
            human_answer_namber = int(human_answer_string)
            break
        except ValueError:
            print("Повторите ввод действия")
            continue
    
    if human_answer_namber == 1:
        flag_for_format_safe_data = "column"
    elif human_answer_namber == 2:
        flag_for_format_safe_data = "line"

    return flag_for_format_safe_data