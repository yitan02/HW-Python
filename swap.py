def swap_last_item():
    list = []
    for i in range (n):
        data = int(input())
        list.append(data)
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp
    return list
