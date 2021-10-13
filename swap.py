
def swap_last_item(list):
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp
    return list
