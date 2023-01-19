#Calculator

#Add
def add (n1, n2):
  """Adds two inputted parameters together"""
  return n1 + n2

#Subtract
def subtract(n1, n2):
  """Subtracts 2nd inputted parameter from first input"""
  return n1 - n2

#Multiply
def multiply(n1, n2):
  """Multiplies two inputted parameters"""
  return n1 * n2

#Divide
def divide(n1, n2):
  """Dividies first inputted paramete by second parameter"""
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

symbol_string = ""
for symbol in operations:
  symbol_string += symbol + " "

operation_symbol = input(f"Pick an operation [{symbol_string}]: ")

answer = (operations[operation_symbol])(num1,num2)
                            
print(f"{num1} {operation_symbol} {num2} = {answer}")