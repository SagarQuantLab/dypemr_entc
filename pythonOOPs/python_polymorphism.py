class classOne:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2
    
class classTwo:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def multiplication(self):
        return self.num1 * self.num2
    
class childClass(classOne, classTwo):

    def __init__(self, num1, num2):
        super().__init__(num1, num2)
    
    