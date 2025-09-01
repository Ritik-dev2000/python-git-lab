#calculator
class Calculator:
    def add(self, a, b):
        return a + b
calc  = Calculator()
a,b =int(input("First")),int(input("Second"))
print("Sum:",calc.add(a,b))