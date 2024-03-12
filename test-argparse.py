import argparse
parser = argparse.ArgumentParser(description='Calculadora')
parser.add_argument('--suma', type=int, help='Suma dos números')
args = parser.parse_args()
result = args.suma
print("Resultado", args.suma, "+ 2 = ", result)