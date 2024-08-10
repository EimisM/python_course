from typing import Tuple

def math(a: int, b: int) -> Tuple[int, int, float, float]:
    addition = a + b
    subtract = a - b
    division = a / b
    multiply = a * b
    return addition, subtract, division, multiply