def tripler(func):
    def wrapper():
       """
    Calls a function 3 times.
      
    This function has nothing much special and calls a function three times.
    
    Parameter
    _________
    func : function
        A function with code that the decorator calls.
    
    Returns
    _______
    function
        Outputs results of a function
    
    Example
    _______
    >>> tripler(func)
    # say the function adds 2+2
    4
    4
    4
    >>> tripler(func)
    # say the function prints "hello"
    hello
    hello
    hello
    """
       func()
       func()
       func()
    return wrapper
