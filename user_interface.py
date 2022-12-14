import load_and_safe_data as l_s_d
import print_data
import add_data
import delete_data
import search_data
import choosing_action_for_user_interface as action_user
import removing_repetitions as del_rep_rec

def work_phone_directory():

    data = l_s_d.loading_data_from_phone_directory()
    
    while True:
        action = action_user.choosing_start_work_action()
        match action:
            case 1:
                print_data.print_all_list_in_terminal(data)
            case 2:
                data.append(add_data.input_data_in_phone_directory())
            case 3:
                data = delete_data.delet_data_from_list(data)
            case 4:
                data = del_rep_rec.delet_repeat_data(data)
            case 5:
                work_phone_submenu()
            case 6:
                data = l_s_d.loading_data_from_phone_directory()
            case 7:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data))
            case 8:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data), "column")
            case 9:
                print("данные не сохранены")
                return True
            case 10:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data),\
                    action_user.choosing_action_for_safe())
                print("данные сохранены")
                return True

def work_phone_submenu():

    data = l_s_d.loading_data_from_phone_directory()
    data_from_search = search_data.search_data_from_list(data) 
    while True:
        action = action_user.choosing_action_submenu()
        match action:
            case 1:
                data_from_search = search_data.search_data_from_list(data)     
            case 2:
                print_data.print_all_list_in_terminal(data)
            case 3:
                data = delete_data.delet_data_from_serch_list(data, data_from_search)
            case 4:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data))
                work_phone_directory()