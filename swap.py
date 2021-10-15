
def swap_last_item(list):
    input = list 
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp
    print(list[0])
    output = []
    output.append(list[0])
    output.extend(list[1:-1])
    output.append(list[-1])
    print(f'Input: {input}')
    print(f'Output: {output}')
    return list
