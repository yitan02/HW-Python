def calculator(number1,number2,operator):
       converted_number1 = str(number1)
       converted_number2 = str(number2) 
      # message = input("Enter equation: ")
      # for character in message:
      #     if character not in '+-*/' or character not in '1234567890':
      #          return False 
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

