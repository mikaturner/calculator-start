#Calculator
from art import logo

#Add
def add (n1, n2):
  """Adds two input parameters together"""
  return n1 + n2

#Subtract
def subtract(n1, n2):
  """Subtracts 2nd input parameter from first input"""
  return n1 - n2

#Multiply
def multiply(n1, n2):
  """Multiplies two input parameters"""
  return n1 * n2
    
#Divide
def divide(n1, n2):
  """Divides first input parameter by second parameter"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  num1 = float(input("What's the first number?: "))
  
  symbol_string = ""
  for symbol in operations:
    symbol_string += symbol + " "
  
  another_calc = True
  
  while another_calc: 
    operation_symbol = input(f"Pick an operation [{symbol_string}]: ")
    
    num2 = float(input("What's the next number?: "))
    
    answer = (operations[operation_symbol])(num1,num2)
                                
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    calculate_more = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:  ")
    if calculate_more == 'y':
      another_calc = True
      num1 = answer
    else:
      another_calc = False
      calculator()

calculator()