n1 = int(input("N1"))
n2 = int(input("N2"))
a = input("Operator")
def calc(n1, a, n2):
    if a == '+':
        print(n1+n2)
    if a == '-':
        print(n1-n2)
    if a == '/':
        print(float(n1/n2))
    if a == '.':
        print(n1*n2)

calc(n1, a, n2)