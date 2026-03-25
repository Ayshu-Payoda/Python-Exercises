def calc_add(n1,n2):
    sum = n1 + n2
    return sum
def calc_sub(n1,n2):
    sub = n1 - n2
    return sub
def calc_mult(n1,n2):
    mult = n1 * n2
    return mult
def calc_div(n1,n2):
    div = n1 / n2
    return int(div)

a = int(input("Enter value a : "))
b = int(input("Enter value b : "))
c = input("Enter operator : ")
if c == "+":
    print(calc_add(a,b))
elif c == "-":
    print(calc_sub(a,b))
elif c == "*":
    print(calc_mult(a,b))
elif c == "/":
    print(calc_div(a,b))
else:
    print("Enter a valid operator")