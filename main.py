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