def input_data_in_phone_directory() -> list:
    
    count = 0
    
    resalt_human_answer = list()
    
    requested_data = ("фамилию", "имя", "отчество", "номер тефена")
    
    while True:
        
        human_answer_string = input(f"Введите {requested_data[count]}: ")
        
        if count >= 3 and not human_answer_string.isdigit():
            print("Повторите ввод телефонного номера")
            continue

        try:
            data = human_answer_string
        except ValueError:
            print("Повторите ввод")
            continue
        else:
            resalt_human_answer.append(data)
            count +=1
            if count == 4: break
    
    return resalt_human_answer