
from art import logo

print(logo)

def add(n1,n2):
    """Function to add two numbers together a return a result """
    return n1 + n2 

def substract(n1,n2):
    """Function to substitute two numbers together a return a result """
    return n1 - n2 

def multiply(n1,n2):
    """Function to multiply two numbers together a return a result """
    return n1 * n2 

def divide(n1,n2):
    """Function to devide two numbers together a return a result """
    return n1 / n2 

operations = {  "+" : add, "-" : substract, "*" : multiply, "/" : divide }

num1 = float(input("What is the first number..?\n"))
num2 = float(input("What is the second number..?\n")) 
symbols = []
for symbol in operations:
    symbols.append(symbol)
operation_symbol = input(f"Which operation do you want to perform..? {symbols} \n")

calculate = operations[operation_symbol]
result = calculate(num1,num2)
print(f"{ num1 } {operation_symbol } { num2 } = { result}")
