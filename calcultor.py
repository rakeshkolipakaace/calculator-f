import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    return a+b
   

def subtract():
    return

def multiply():
    return

def divide():
    return

def modulus():
    return


def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()
    print(f"Values received: a = {a}, b = {b}")
    print(f"Addition of {a} and {b} is {add(a,b)}")
    

if __name__ == "__main__":
    calculator()
