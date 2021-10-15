
def swap_last_item(list):
    input = list 
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp
    output = list
    print(f'Input: {input}')
    print(f'Output: {output}')
    return list
