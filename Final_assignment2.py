##assignment 2
class stringoperation:
    def __init__(self):
        self.s = " "

    def getString(self):
        print("Enter your word: ")
        self.s = str(input())

    def printString(self):
        print("The upper case of your entry is: ")
        print(self.s.upper())



Test1 = stringoperation()
Test1.getString()
Test1.printString()
