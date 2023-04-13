def calcule(num1, operator, num2):
    if operator == "+":
        return num1+num2
    elif operator == "-":
        return num1-num2
    elif operator == "*":
        return num1*num2
    elif operator == "/":
        return num1/num2
    elif operator == "%":
        return num1%num2
    else:
        return "Opérateur invalide"

print(calcule(10, "+", 4))