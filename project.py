def find_max(numbers_list):
    if not numbers_list:
        return None
    current_max = numbers_list[0]
    for i in range(1, len(numbers_list)):
        if numbers_list[i] > current_max:
            current_max = numbers_list[i]
    return current_max


print(find_max([]))

