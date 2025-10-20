"""
calculadora.py
Script simple que emula una calculadora con las 4 operaciones básicas.
Pide dos operandos y la operación por consola, maneja entradas inválidas
y división por cero.
"""
from __future__ import annotations
from typing import Callable, Dict


def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("No es posible dividir por cero.")
    return a / b


_OPERACIONES: Dict[str, Callable[[float, float], float]] = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir,
}


def solicitar_numero(prompt: str) -> float:
    """Solicita repetidamente un número hasta que la entrada sea válida."""
    while True:
        texto = input(prompt).strip()
        if texto.lower() in ("q", "salir", "exit"):
            raise KeyboardInterrupt
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Introduce un número o 'q' para salir.")


def solicitar_operacion(prompt: str) -> str:
    """Solicita una operación válida (+, -, *, /)."""
    while True:
        op = input(prompt).strip()
        if op.lower() in ("q", "salir", "exit"):
            raise KeyboardInterrupt
        if op in _OPERACIONES:
            return op
        print("Operación inválida. Usa +, -, * o / (o 'q' para salir).")


def calcular(a: float, b: float, op: str) -> float:
    func = _OPERACIONES[op]
    return func(a, b)


def main() -> None:
    print("Calculadora simple. Escribe 'q' en cualquier entrada para salir.")
    try:
        a = solicitar_numero("Primer operando: ")
        b = solicitar_numero("Segundo operando: ")
        op = solicitar_operacion("Operación (+, -, *, /): ")
        try:
            resultado = calcular(a, b, op)
        except ZeroDivisionError as exc:
            print(f"Error: {exc}")
            return
        # Muestra resultado con eliminación de ceros innecesarios
        if resultado.is_integer():
            print(f"Resultado: {int(resultado)}")
        else:
            print(f"Resultado: {resultado}")
    except KeyboardInterrupt:
        print("\nSaliendo. ¡Hasta luego!")


if __name__ == "__main__":
    main()