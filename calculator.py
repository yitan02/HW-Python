def calculator(number1,number2,operator):
       print('python calculator.py')
       print("") 
       print(f'Enter equation: {number1} {operator} {number2}')
       for character in operator:
           if character not in '+-*/':
                return False 
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
    number1 = user_input.split()[0]
    operator = user_input.split()[1]
    number2 = user_input.split()[2]
    calculator(number1,number2,operator)

