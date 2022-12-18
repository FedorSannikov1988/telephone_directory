import validation
def choosing_start_work_action():

    print("\n")
    print("\t       ЗАПУЩЕН ТЕЛЕФОННЫЙ СПРАВОЧНИК")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  просмотреть все записи в справочнике")
    print("\t 2 -  отсортировать записи в справочнике")
    print("\t 3 -  добавить запись в справочник")
    print("\t 4 -  удалить запис(-и)(-ь) из справочника")
    print("\t 5 -  удалить повторяющиеся записи")
    print("\t 6 -  найти запись в справочнике")
    print("\t 7 -  загрузить данные (данные загруженные")
    print("\t      ранее будут утеряны)")
    print("\t 8 -  выход")
    print("")
    
    return validation.validation_answer_number(1, 8)

def choosing_action_submenu():
    print("\n")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  повторить поиск")
    print("\t 2 -  изменить запись в справочнике")
    print("\t 3 -  удалить запис(-и)(-ь) из справочника")
    print("\t 4 -  вернуться в основное меню")  
    print("") 

    return validation.validation_answer_number(1, 4)   

def choosing_action_submenu_exit():
    print("\n")
    print("\t","*"*41)
    print("\t Выберите действие:")
    print("\t 1 -  выйти из справочника и сохранить в формате: line")
    print("\t 2 -  выйти из справочника и сохранить в формате: column")
    print("\t 3 -  выйти без сохранения")
    print("\t 4 -  вернуться в основное меню")  
    print("") 

    return validation.validation_answer_number(1, 4)  

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

    human_answer_number = validation.validation_answer_number(1, 2)
    
    if human_answer_number == 1:
        flag_for_format_safe_data = "column"
    elif human_answer_number == 2:
        flag_for_format_safe_data = "line"

    return flag_for_format_safe_data
