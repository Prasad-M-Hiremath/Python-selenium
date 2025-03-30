class Calculator:
    num=1100


    def __init__(self,a,b):        #CREATING CONSTRUCTOR
        print("This is constructor")
        self.a=a
        self.b=b


    # CREATING METHOD
    def getData(self):    #CREATING METHOD
        print("This is method creation")

    def sum(self):
        return self.a + self.b + Calculator.num



#CREATING OBJECTS
obj=Calculator(2,3)   #CREATING OBJECTS
obj.getData()
print(obj.sum())

obj=Calculator(8,3)   #CREATING OBJECTS
obj.getData()
print(obj.sum())