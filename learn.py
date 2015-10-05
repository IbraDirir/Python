#default paramaters and Multiple Arguments
#student score
def studentScore(name, score):
    print(name, "Scored", score,"Marks")
studentScore("Ibra", 99)
#default paramater

def studentScore(name="tom", score=0):
    print(name,"got", score, "points")

studentScore("mark",100)#you can overwrite default paramaters

#passing multiple values to one paramater
#wild cards
def studentScores(name,*score):
    print(name,"scores",score, "Marks")
studentScores("mark", 89, 90, 100, 100, 78)


#Classes
class Person:
    #initiliazing a class constructor
    def __init__(self):

        print("no need for explicit calling")
    def __del__(self):
        print("Our class  instance is distroyed")
    def setFullName(self,FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    def printFullName(self):
        print(self.FirstName, " ", self.LastName)
personName = Person()
personName.setFullName("Ibrahim", "Dirir")
personName.printFullName()
personName.__del__()


#inheritance
#inheritance allows us to define a
#class in terms of anather
#class, which makes it easier
#to  create and  maintain  an application

class Parent:
    value1 = "this is value 1"
    value2 = "this is value 2"
class Child(Parent):
    pass
parent_=Parent()
print(parent_.value1)

print(parent_.value2)
child_=Child()
print(child_.value1)

print(child_.value2)

