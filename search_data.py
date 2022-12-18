import logger

def search_data_from_list(all_data: list, need_find_data: list) -> list:
    
    logger.log_entry(str(need_find_data))
    
    data_from_serch = []

    for count in range(0, len(all_data), 1):
        if [all_data[count][0]].count(need_find_data[0]) or\
            [all_data[count][1]].count(need_find_data[1]) or\
                [all_data[count][2]].count(need_find_data[2]) or\
                    [all_data[count][3]].count(need_find_data[3]):
                    data_from_serch.append(all_data[count])

    return data_from_serch