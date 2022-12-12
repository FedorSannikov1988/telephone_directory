import load_and_safe_data as l_s_d
import print_data
import add_data
import delete_data
import search_data
import choosing_action_for_user_interface as action_user

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
                print("еще не написали ожитется в ближайшее время")
            case 5:
                l_s_d.safe_data_in_phone_directory(data,action_user.choosing_action_for_safe())
                print("данные сохранены")
                break