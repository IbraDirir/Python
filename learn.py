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