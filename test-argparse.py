import argparse
parser = argparse.ArgumentParser(description='Calculadora')
parser.add_argument('--s', type=str, help='Suma dos números')
parser.add_argument('--r', type=str, help='Suma dos números')
parser.add_argument('--m', type=str, help='Suma dos números')
parser.add_argument('--d', type=str, help='Suma dos números')
args = parser.parse_args()
z = 0
valors = args.s.split(" ")
valors = args.r.split(" ")
valors = args.m.split(" ")
valors = args.d.split(" ")
for valor in valors:
    z = z+int(valor)
print(z)