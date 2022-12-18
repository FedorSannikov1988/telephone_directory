import load_and_safe_data as l_s_d
import print_data
import add_data
import delete_data
import search_data
import choosing_action_for_user_interface as action_user
import removing_repetitions as del_rep_rec
import change_data
import sort_data
import logger

def work_phone_directory():

    data = l_s_d.loading_data_from_phone_directory()
    logger.log_entry("запуск справочника")

    while True:

        action = action_user.choosing_start_work_action()
        
        match action:
            case 1:
                logger.log_entry("показать все записи в справочнике")
                print_data.print_all_list_in_terminal(data)
            case 2:
                logger.log_entry("отсортировать записи в справочнике")  
                data = sort_data.sorting_data(data)
            case 3:
                logger.log_entry("добавить запись в справочник")
                data.append(add_data.input_data_in_phone_directory())
            case 4:
                logger.log_entry("удалить запис(-и)(-ь) из справочника")
                data = delete_data.delet_data_from_list(data)
            case 5:
                logger.log_entry("удалить повторяющиеся записи")
                data = del_rep_rec.delet_repeat_data(data)
            case 6:
                logger.log_entry("найти запись в справочнике")
                data = submenu_for_search(data)
            case 7:
                logger.log_entry("загрузить данные (данные загруженные ранее будут утеряны)")
                data = l_s_d.loading_data_from_phone_directory()
            case 8:
                logger.log_entry("меню выхода")
                if submenu_for_exit(data) == False: break


def submenu_for_search(data):

    data_from_search = search_data.search_data_from_list(data, add_data.input_data_in_phone_directory())
    
    print_data.print_all_list_in_terminal(data_from_search)
 
    while True:
        
        action_submenu = action_user.choosing_action_submenu()

        match action_submenu:
            
            case 1:
                data_from_search = search_data.search_data_from_list(data, add_data.input_data_in_phone_directory()) 
                print_data.print_all_list_in_terminal(data_from_search)
                     
            case 2:
                data = change_data.change_data_in_telephone_directory(data, data_from_search)

            case 3:
                data = delete_data.delet_data_from_serch_list(data, data_from_search)
                
            case 4:
                return data


def submenu_for_exit(data):

    while True:

        action_submenu_exit = action_user.choosing_action_submenu_exit()

        match action_submenu_exit:
            case 1:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data))
                print("данные сохранены в формате line")
                return False
            case 2:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data), "column")
                print("данные сохранены в формате column")
                return False
            case 3:
                print("данные не сохранены")
                return False
            case 4:
                return True