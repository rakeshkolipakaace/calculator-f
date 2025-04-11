import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    return a+b
   

def subtract(a,b):
    return a-b
  
def multiply(a, b):
    return a*b

def divide(a,b):
    if(b!=0):
        return a/b
    else:
        return math.inf

def modulus(a,b):
    return a%b


def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()
    print(f"Values received: a = {a}, b = {b}")
    print(f"Addition of {a} and {b} is {add(a,b)}")
    print(f"Subtraction of {a} and {b} is {subtract(a,b)}")
    print(f"Multiplication of {a} and {b} is {multiply(a,b)}")
    print(f"Division of {a} and {b} is {divide(a,b)}")
    print(f"Modulos of {a} and {b} is {modulus(a,b)}")
if __name__ == "__main__":
    calculator()
