#practical example of while loop
a = 1
s = 0
print("Enter Numbers to add to the sum. ")
print('Enter 0 to quit. ')
while a != 0:
    print('currents sum: ', s)
    a = float(input('Numbers?'))
    a = float(a)
    s += a #s = s + a
print('Total sum = ',s)