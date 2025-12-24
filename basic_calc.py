print("what do you want to do?")
print("1- addition") 
print("2- subtraction") 
print("3- multiplacation") 
print("4- division") 

select = int(input("select an operator (use integer to select 1-4): "))
# need to add multiple inputs istead of just a and b 
def add(a, b): 
    c = a + b 
    return c

def sub(a, b): 
    c = a - b
    return c

def mult(a, b): 
    c = a * b
    return c

def div(a, b):
    c = a / b
    return c 

if select == 1:
    a = float(input("1st digit: "))
    b = float(input("2nd digit: ")) 
    print(f"{a} + {b} = {add(a, b)}") 
elif select == 2:
    a = float(input("1st digit: "))
    b = float(input("2nd digit: ")) 
    print(f"{a} - {b} = {sub(a, b)}") 
elif select == 3:
    a = float(input("1st digit: "))
    b = float(input("2nd digit: ")) 
    print(f"{a} * {b} = {mult(a, b)}") 
elif select == 4:
    a = float(input("1st digit: "))
    b = float(input("2nd digit: ")) 
    if b != 0:
        print(f"{a} / {b} = {div(a, b)}") 
    else:
        print("Cannot divide by zero!") 
else:
    print("Invalid selection!")
