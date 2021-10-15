def calculator(number1,number2,operator):
       converted_number1 = str(number1)
       converted_number2 = str(number2)
       print('python calculator.py')
       print("") 
       print(f'Enter equation: {number1} {operator {number2}')
       for character in operator:
           if character not in '+-*/':
                return False 
       if operator == '+' :
             return number1 + number2
       elif operator == '-' :
             return number1 - number2
       elif operator == '/' :
             if number2 == 0:
                return
             else:
                return number1/number2
       elif operator == '//' :
             return number1//number2
       elif operator == '**' :
             return number1**number2
       elif operator == '*' :
             return number1*number2

def parse_input(user_input):
    number1 = user_input.split()[0]
    operator = user_input.split()[1]
    number2 = user_input.split()[2]
    calculator(number1,number2,operator)

