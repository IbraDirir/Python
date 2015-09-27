#flexible number of arguments
def add_numbers(*add):
    total =  0
    for  a in add:
        total += a
    print(total)
add_numbers(5)
add_numbers(9,10)
add_numbers(10,100,1000)