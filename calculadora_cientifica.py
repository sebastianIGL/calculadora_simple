import math


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b


def log10_op(a):
    if a <= 0:
        raise ValueError("Logaritmo indefinido para valores <= 0")
    return math.log10(a)


def pow_op(a, b):
    return math.pow(a, b)


def sqrt_op(a):
    if a < 0:
        raise ValueError("Raíz cuadrada de número negativo")
    return math.sqrt(a)


def factorial_op(n):
    if n < 0 or not float(n).is_integer():
        raise ValueError("Factorial solo definido para enteros no negativos")
    return math.factorial(int(n))


def parse_number(s):
    try:
        return float(s)
    except ValueError:
        raise ValueError(f"Entrada numérica inválida: {s}")


def main():
    print("Calculadora Científica")
    print("---------------------")

    try:
        op = input("Ingrese operación (+, -, *, /, log, pow, sqrt, fact): ").strip()
    except (KeyboardInterrupt, EOFError):
        print()
        return

    op = op.lower()

    try:
        if op in {"+", "-", "*", "/", "pow"}:
            a = parse_number(input("Ingrese operando 1: "))
            b = parse_number(input("Ingrese operando 2: "))
            if op == "+":
                res = add(a, b)
            elif op == "-":
                res = sub(a, b)
            elif op == "*":
                res = mul(a, b)
            elif op == "/":
                res = div(a, b)
            else:  # pow
                res = pow_op(a, b)

        elif op == "log":
            a = parse_number(input("Ingrese operando: "))
            res = log10_op(a)

        elif op == "sqrt":
            a = parse_number(input("Ingrese operando: "))
            res = sqrt_op(a)

        elif op in {"fact", "factorial", "!"}:
            a = parse_number(input("Ingrese operando (entero no negativo): "))
            res = factorial_op(a)

        else:
            print("Operación no reconocida")
            return

        if isinstance(res, float) and res.is_integer():
            print(f"El resultado es {int(res)}")
        else:
            print(f"El resultado es {res}")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
