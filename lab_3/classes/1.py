'''Define a class which has at least two methods:
 getString:to get a string from console input printString:
to print the string in upper case.'''
class MyClass:
    def getString(self):
        self.s = input("Enter a string: ")
    def printString(self):
        print(self.s.upper())
my_class = MyClass()
my_class.getString()
my_class.printString()
