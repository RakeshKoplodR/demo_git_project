import math

class Arithmetic_Ops:


    def add(a: float, b: float) -> float:
        return a + b


    def subtract(a: float, b: float) -> float:
        return a - b


    def multiply(a: float, b: float) -> float:
        return a * b


    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


    def power(base: float, exp: float) -> float:
        return base ** exp


    def modulus(a: int, b: int) -> int:
        if b == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return a % b


    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        return math.factorial(n)


    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
