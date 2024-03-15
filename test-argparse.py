import argparse
parser = argparse.ArgumentParser(description='Calculadora')
#Añado cada posible input.
# nargs='+' indica que acepta uno o más valores
#y los convierte en una lista
parser.add_argument('-s', '--suma', nargs='+', type=float, help='Suma números')
parser.add_argument('--r', nargs='+', type=float, help='Resta números')
parser.add_argument('--m', nargs='+', type=float, help='Multiplica números')
parser.add_argument('--d', nargs='+', type=float, help='Divide números')
args = parser.parse_args()

if args.s:
    result = sum(args.s)
    print(result)
elif args.r:
    result = args.r[0] - sum(args.r[1:])
    #toma como inicio el primer número y le resta todos los demás.
    print(result)
elif args.m:
    result = 1
    for val in args.m:
        result *= val
        #result *= val significa lo mismo que result = result * val
    print(result)
elif args.m:
    result = args.d[0]
    for val in args.d:
        if val == 0:
            print("Error! División por cero.")
        result /= val
    print(result)
else:
    print("Invalid input.")
