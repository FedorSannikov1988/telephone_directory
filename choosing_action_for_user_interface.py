def choosing_start_work_action():

    print("\n")
    print("\t       ЗАПУЩЕН ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  просмотреть все записи в справочнике")
    print("\t 2 -  добавить запись в справочник")
    print("\t 3 -  удалить запис(-и)(-ь) из справочника")
    print("\t 4 -  удалить повторяющиеся записи")
    print("\t 5 -  найти запись в справочнике")
    print("\t 6 -  загрузить данные (данные загруженные")
    print("\t      ранее будут утеряны)")
    print("\t 7 -  сохранить данные в формате: line")
    print("\t 8 -  сохранить данные в формате: column")
    print("\t 9 -  выйти из справочника без сохранения")
    print("\t      изминений и удаления повторов")
    print("\t      в телефонной книге")
    print("\t 10 - выйти из справочника с сохранением")
    print("\t      изминений в телефонной книге")
    print("\t","-"*41)
    print("\t Примечание к пункту 10:")
    print("\t При выходе из справочника данные автоматически сохраняются.")
    print("\t Пользователю предоставляеся выбор в каком формате line или")
    print("\t column данные будут сохранены. Так же происходит удаление")
    print("\t повторяющихся записей.")
    print("")

    while True:
        human_answer_string = input(f"Какое действие выбираете: ")
        
        if not human_answer_string.isdigit() or int(human_answer_string) > 10 or int(human_answer_string) < 1 :
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