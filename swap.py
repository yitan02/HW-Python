
def swap_last_item(list):
    input = list 
    temp = list[-1]
    list[-1] = list[0]
    list[0] = temp
    output = []
    output.append(list[-1])
    output.extend(list[1:-1])
    output.append(list[0])
    print(f'Input: {input}')
    print(f'Output: {output}')
    return list
