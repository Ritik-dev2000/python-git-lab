#calculator
class Calculator:
    def add(self, a, b):
        return a + b
<<<<<<< Updated upstream
=======
    def subtract(self, a, b):
        return a - b
    def multiply(self, a, b):
        return a * b    
>>>>>>> Stashed changes
calc  = Calculator()
a,b =int(input("First")),int(input("Second"))
print("Sum:",calc.add(a,b))