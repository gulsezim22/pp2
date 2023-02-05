class TwoClasses:
    def __init__(self):
        self.s1=""
    def getString(self):
        self.s1=input()
    def printString(self):
        print(self.s1.upper())
s1 = TwoClasses()
s1.getString()
s1.printString()