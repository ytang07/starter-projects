def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a, b):
    return a/b

operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

def perform(a, op, b):
    func = operations[op]
    return func(int(a), int(b))

print("This calculator takes two numbers and performs a basic operation")
a = input("What is the first number? ")
op = input("Which operation would you like to perform? (add, subtract, multiply, or divide) ")
b = input("What is the second number? ")

print(perform(a, op, b))
