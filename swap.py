def swap_last_item(list):
    """
    Swap the first item of the list with the last item.
 
    This function takes the last item and store it in a temporary variable. 
    Then, it set its last item to the first item. Lastly, the first item 
    takes in the last item, completing the swapping. Input and output lists are
    printed for visualization.

    Parameters
    __________
    list : list of int
         A list of integers inputted.

    Returns
    _______
    list : list of int
        A list where the first and last item is swapped.

    Examples
    --------
    >>> A = [1,2,3]
    [3,2,1]
    >>> B = [100,14,56,98,2,4]
    [4,14,56,98,2,100]
    """

    input = list
 
    #stored last item in temp so that the last item can still be used after
     swapping
    temp = list[-1]
 
    list[-1] = list[0]
    list[0] = temp

    #created an empty list called output and added values in to be printed
    output = []
    output.append(list[-1])
    output.extend(list[1:-1])
    output.append(list[0])

    print(f'Input: {input}')
    print(f'Output: {output}')

    return list
