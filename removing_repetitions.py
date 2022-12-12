def delet_repeat_data(data_in: list) -> list:
    data_out = list()
    [data_out.append(element) for element in data_in if element not in data_out]
    return data_out