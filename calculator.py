#calculator
class Calculator:
    def add(self, a, b):
        return a + b
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b    
calc  = Calculator()
a,b =int(input("First")),int(input("Second"))
print("Sum:",calc.add(a,b))
print("Difference:",calc.subtract(a,b))
print("Product:",calc.multiply(a,b))