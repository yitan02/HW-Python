def calculator(number1,number2,operator):
     
   # Perform operations on two numbers based. 

   # This function takes the operator and calculate the result from the two 
   # numbers. The type of operation it will perform will be dependent on the
   # user's input. There is also complex division added in to prevent division
   # by zero.

   # Parameter
   #  _________
   # number1 : int
   #        First number to perform operation.
   # number2 : int 
   #        Second number to perform operation.
   # operator : str
   #        An operation symbol to determine operation performed.
    
   # Returns
   # _______
   # int
   #    The sum, subtraction,integer division, power, multiplication of
   #    "number1" and "number2".
   # float
   #    The simple division of "number1" and "number2".

   # Examples
   # ________
   # >>> calculator(1,1,'+')
   # 2
   # >>> calculator(4,2,'-')
   # 2
   # >>> calculator(10,5,'/')
   # 2.0
   # >>> calculator(20,5,'//')
   # 4
   # >>> calculator(2,4,'*')
   # 8
   # >>> calculator(5,2,'**')
   #25
   #"""

    print('python calculator.py')
    print("") 
    print(f'Enter equation: {number1} {operator} {number2}')

    # Checking if the character is a valid operator
     for character in operator:
         if character not in '+-*/':
            return False
   
    # Performing operation based on input operator
     if operator == '+' :
          sum = number1 + number2
          print(sum)
          return sum
     elif operator == '-' :
          difference = number1-number2
          print(difference)
          return difference
     elif operator == '/' :
         if number2 == 0:
             print('cannot print by 0')
             return
         else:
             divide = number1/number2
             print(divide)
             return divide
     elif operator == '//' :
          int_div = number1//number2
          print(int_div)
          return int_div
     elif operator == '**' :
          power = number1**number2
          print(power)
          return power
     elif operator == '*' :
          multiply = number1*number2
          print(multiply)
          return multiply

def parse_input(user_input):
    """
    Split the number and operator.
   
    The function splits the number and operator so that it is easy to use as
    a variable in calculator(). The parse items will be assigned to input 
    variables for calculator() and call on calculator(). 
    
    Parameter
    _________
    user_input : tuple of (int, str, int)
              Contains numbers and operator string to parse.
    
    Return
    ______
    int
       The parse integers from user_input
    str
       The parse string operator from user_input
    
    Examples
    ________
    >>> parse_input(10+1)
    ['10','+','1']
    >>> parse_input(25**2)
    ['25','**','2']
    >>> parse_input(99-4)
    ['99','-','4']
    """ 
   
    # Assign parse item to variables that will be used for calculator()
    number1 = user_input.split()[0]
    operator = user_input.split()[1]
    number2 = user_input.split()[2]

    calculator(number1,number2,operator)

