from pathlib import Path
import datetime

file_name = "log_of_operator_actions.csv"
relative_file_directory = Path(file_name)

def log_entry(data_for_write: str) -> None:
    
    d_t_n = datetime.datetime.now()

    global relative_file_directory

    with open(relative_file_directory, 'a', encoding='utf-8') as data:
        data.write("|{}_{}_{}|{}_{}_{}|done action: {}\n".format(d_t_n.day, d_t_n.month,\
             d_t_n.year, d_t_n.hour, d_t_n.minute, d_t_n.second, data_for_write))