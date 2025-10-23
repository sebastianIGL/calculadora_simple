def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero")
    return a / b


_OPERACIONES = {"+": sumar, "-": restar, "*": multiplicar, "/": dividir}


def _leer_numero(prompt):
    while True:
        texto = input(prompt).strip()
        if texto.lower() in ("q", "salir", "exit"):
            raise KeyboardInterrupt
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Introduce un número o 'q' para salir.")


def _leer_operacion(prompt):
    while True:
        op = input(prompt).strip()
        if op.lower() in ("q", "salir", "exit"):
            raise KeyboardInterrupt
        if op in _OPERACIONES:
            return op
        print("Operación inválida. Usa +, -, * o / (o 'q' para salir).")


def main():
    print("Calculadora simple. Escribe 'q' para salir en cualquier momento.")
    try:
        a = _leer_numero("Primer operando: ")
        b = _leer_numero("Segundo operando: ")
        op = _leer_operacion("Operación (+, -, *, /): ")
        try:
            resultado = _OPERACIONES[op](a, b)
        except ZeroDivisionError:
            print("Error: División por cero")
            return
        # Mostrar resultado (mostrar entero si corresponde)
        if isinstance(resultado, float) and resultado.is_integer():
            print("Resultado:", int(resultado))
        else:
            print("Resultado:", resultado)
    except KeyboardInterrupt:
        print("\nSaliendo.")


if __name__ == "__main__":
    main()