class Shape(object):
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length2):
        Shape.__init__(self)
        self.length = length2
    def area(self):
        return self.length*self.length
integer1=Square(5)
print(integer1.area())