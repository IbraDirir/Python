#default paramaters and Multiple Arguments
#student score
def studentScore(name, score):
    print(name, "Scored", score,"Marks")
studentScore("Ibra", 99)
#default paramater

def studentScore(name="tom", score=0):
    print(name,"got", score, "points")
studentScore()