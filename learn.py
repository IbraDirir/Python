fw = open("sample.txt", "w")
fw.write("writing stuff in my file\n")
fw.write("cool")
fw.close()
fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()
#function inside lists
def list_function(x):

    x[1] = x[1] + 3
    return x

n = [3, 5, 7]
print(list_function(n))

