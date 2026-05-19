def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return float('inf')
    return a / b

def power(a, b):
    """Возводит a в степень b. При отрицательной степени возвращает float."""
    return a ** b