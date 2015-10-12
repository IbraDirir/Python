user_string = input("what is your word? ")
user_num = input("what is your num? ")
try:
    myNum = int(user_num)
except:
    myNum = float(user_num)
if not "." in user_num:
    print(user_string[myNum])
else:
    ratio = round(len(user_string)*myNum)
    print(user_string[ratio])
