class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length2, width2):
        Shape.__init__(self)
        self.length = length2
        self.width=width2
    def area(self):
        return self.length*self.width
integer1=Rectangle(5,2)
print(integer1.area())