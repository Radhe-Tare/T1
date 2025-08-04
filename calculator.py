print("Welcome to the Calculator!\n")

def operate(x,y,z):
    if z in {"1","add", "additon"}:
        return x + y
    if z in {"2","sub", "subtract"}:
        return x - y
    if z in {"3","mul","multiply"}:
        return x * y
    if z in {"4","div","divide"}:
        return x / y
    
    return None    

check = {"1","2","3","4","5","add","sub","mul","div","exit","addition","subtract","multiply","divide"}

print("Select operation:")
print("1. Add (add, addition)")
print("2. Subtract (sub, subtract)")
print("3. Multiply (mul, multiply)")
print("4. Divide (div, divide)")
print("5. Exit (exit)\n\n")


while True:
    while True:
        choice = (input("Enter choice : ")).lower().strip()
        if choice in check:
            break
        else:
            print("Invalid input. Please try again.\n")
    
    if choice in {"5","exit"}:
        print("! Thank you !")
        break

    n1 = float(input("Enter first number : "))
    n2 = float(input("Enter second number : "))

    result = operate(n1, n2, choice)
    print(f"Result: {result}\n\n")