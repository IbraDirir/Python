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
    def setFullName(self,FirstName, LastName):
        self.FirstName = FirstName
        self.LastName = LastName
    def printFullName(self):
        print(self.FirstName, " ", self.LastName)
personName = Person()
personName.setFullName("Ibrahim", "Dirir")
personName.printFullName()



