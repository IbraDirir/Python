#variable scope
a = 101
def ibra():
    print(a)

def jamila():
    print(a)

ibra()
jamila()

#keyword arguments

def safari(name = "ibrahim",  did = "went",  where = "to Mombasa"):
    print(name, did,where)

safari()
safari("jamila", "went", "to Mombasa")
safari(did =  "left", where = "Nairobi")