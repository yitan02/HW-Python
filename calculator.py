def calculator(number1,number2,operator):
    allowed = set("+ - * / // **")
    while True:
          message = input("Enter equation: ")
          if message and allowed.issuperset(message):
             return False 
          if operator == '+'
             return number1 + number2
          else if operator == '-'
             return number1 - number2
          else if operator == '/'
             return number1/number2
          else if operator == '//'
             return number1//number2
          else if operator == '**'
             return number1**number2

def parse_input(user_input):
    number1 = user_input.split()[0]
    operator = user_input.split()[1]
    number2 = user_input.split()[2]
    calculator(number1,number2,operator)

