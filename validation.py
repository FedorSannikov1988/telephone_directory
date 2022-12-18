def validation_answer_number(min_number: int, max_number: int):
    while True:
        human_answer_string = input(f"Какое действие выбираете: ")
        
        if not human_answer_string.isdigit() or int(human_answer_string) > max_number or int(human_answer_string) < min_number:
            print("Повторите ввод действия")
            continue

        try:
            human_answer_number = int(human_answer_string)
            break
        except ValueError:
            print("Повторите ввод действия")
            continue
    
    return human_answer_number