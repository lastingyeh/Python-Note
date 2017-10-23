class Calculator:
    name = 'calculator'
    price = 18

    def __init__(self, name, price, height=20, weight=25, width=30):
        self.name = name
        self.price = price
        self.height = height
        self.weight = weight
        self.width = width

    def add(self, x, y):
        print(self.name)
        return x + y

    def minus(self, x, y):
        return x - y

    def times(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


cal = Calculator('test', 12, 30)

print(cal.name)
print(cal.weight)

# print(cal.name)
#
# print(cal.add(5, 6))
# print(cal.minus(6, 5))
# print(cal.times(6, 5))
# print(cal.divide(10, 5))
