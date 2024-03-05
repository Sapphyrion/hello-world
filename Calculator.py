#suma
def suma(x, y):
    return x+y
#resta
def resta(x, y):
    return x-y
#multiplicación
def multiplicar(x, y):
    return x*y
#división
def dividir(x, y):
    return x/y
#input
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide")
while True:
    oper = input("Select an option (1/2/3/4): ")
    if oper == "1":
        x = int(input("Input the first number: "))
        y = int(input("Input the second number: "))
        print(x, "+", y, "=", suma(x, y))
    if oper == "2":
        x = int(input("Input the first number: "))
        y = int(input("Input the second number: "))
        print(x, "-", y, "=", resta(x, y))
    if oper == "3":
        x = int(input("Input the first number: "))
        y = int(input("Input the second number: "))
        print(x, "*", y, "=", multiplicar(x, y))
    if oper == "4":
        x = int(input("Input the first number: "))
        y = int(input("Input the second number: "))
        print(x, "/", y, "=", dividir(x, y))
    next = input("Would you like to continue? (Yes/No) ")
    if next == "No":
        break
    if next == "no":
        break
