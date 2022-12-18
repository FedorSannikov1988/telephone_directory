import load_and_safe_data as l_s_d
import print_data
import add_data
import delete_data
import search_data
import choosing_action_for_user_interface as action_user
import removing_repetitions as del_rep_rec
import change_data
import sort_data

def work_phone_directory():

    data = l_s_d.loading_data_from_phone_directory()
    
    while True:
        action = action_user.choosing_start_work_action()
        match action:
            case 1:
                print_data.print_all_list_in_terminal(data)
            case 2:
                data = sort_data.sorting_data(data)    
            case 3:
                data.append(add_data.input_data_in_phone_directory())
            case 4:
                data = delete_data.delet_data_from_list(data)
            case 5:
                data = del_rep_rec.delet_repeat_data(data)
            case 6:
                work_phone_submenu(data)
            case 7:
                data = l_s_d.loading_data_from_phone_directory()
            case 8:
                flag_exit = work_phone_submenu_exit(data)
        # if flag_exit == False: 
        #     break        


def work_phone_submenu(data):
    # data_from_search =  print_data.print_all_list_in_terminal(\
    #                 search_data.search_data_from_list(\
    #                     data, add_data.input_data_in_phone_directory()))
    data_from_search = search_data.search_data_from_list(data) 
    while True:
        action_submenu = action_user.choosing_action_submenu()
        match action_submenu:
            case 1:
                data_from_search = search_data.search_data_from_list(data)
                # data_from_search = print_data.print_all_list_in_terminal(\
                #     search_data.search_data_from_list(\
                #         data, add_data.input_data_in_phone_directory()))
                     
            case 2:
                change_data.change_data_in_telephone_directory(data, data_from_search)
                
            case 3:
                data = delete_data.delet_data_from_serch_list(data, data_from_search)
                
            case 4:
                return data

def work_phone_submenu_exit(data):

    while True:
        action_submenu_exit = action_user.choosing_action_submenu_exit()
        match action_submenu_exit:
            case 1:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data))
                print("данные сохранены")
                return False
            case 2:
                l_s_d.safe_data_in_phone_directory(del_rep_rec.delet_repeat_data(data, "column"))
                print("данные сохранены")
                return False
            case 3:
                print("данные не сохранены")
                return False
            case 4:
                return True
         
